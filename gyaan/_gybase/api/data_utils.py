from django.db.models import Model, QuerySet
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


class BaseDataUtils:
    model_class = None

    def get(self, locked=False, **kwargs) -> Model | None:
        try:
            if locked:
                return self.model_class.objects.select_for_update(
                    nowait=True).get(**kwargs)
            else:
                return self.model_class.objects.get(**kwargs)
        except ObjectDoesNotExist:
            return None
        except MultipleObjectsReturned:
            return None

    def filter(self, locked=False, **kwargs) -> QuerySet:
        if locked:
            return self.model_class.objects.filter(
                **kwargs).select_for_update(nowait=True)
        else:
            return self.model_class.objects.filter(**kwargs)

    def update(self, instance: Model, **kwargs) -> Model:
        for attr, value in kwargs.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def create(self, **kwargs) -> Model:
        return self.model_class.objects.create(**kwargs)

    def bulk_update(self, instances: list, fields: list, is_dict=False) -> Model:
        if not is_dict:
            return self.model_class.objects.bulk_update(
                instances, fields, batch_size=500)
        return self.model_class.objects.bulk_update(
            [self.model_class(**i) for i in instances], fields, batch_size=5000)

    def bulk_create(self, objects: list) -> Model:
        return self.model_class.objects.bulk_create(
            [self.model_class(**i) for i in objects], batch_size=500)
        
    def get_fields_as_dict(self, instance: Model, fields=None) -> dict:
        '''
            If fields are given then it returns dictionary with those field as
            key else dictionary with all fields as key against their value for
            one object
        '''
        if fields is None:
            fields = [field.name for field in instance._meta.fields]
        return {field: getattr(instance, field) for field in fields}
