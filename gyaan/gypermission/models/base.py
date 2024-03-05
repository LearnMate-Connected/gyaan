from django.db import models

from django.utils import timezone

from _gybase.models.base import BaseActiveTimeStampModel

from gyproduct.models.base import Product

from gypermission.constants import SUBSCRIPTION_RESOURCE_CHOICES


class Subscription(BaseActiveTimeStampModel):
    
    # Note: Reason of storing ids instead of foreignkey: 
    # We want all our django apps to as decouples as it can be
    subscription_name = models.CharField(help_text="product name + validity + publisher id")
    category = models.CharField(blank=True, null=True)
    resource_type = models.CharField(choices=SUBSCRIPTION_RESOURCE_CHOICES)
    resource_id = models.IntegerField(help_text='Id of resource')
    valid_always = models.BooleanField(default=False)
    validity_days = models.IntegerField(default=0, help_text='Number of valid days for subscription')
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    created_by_id = models.IntegerField()
    consumption = models.IntegerField(default=0)
    limited_consumption_valid = models.BooleanField(default=False)
    
    def __str__(self):
        return "{}-{}-{}".format(self.resource_type, self.resource_id, self.validity_days)
    
    
class UserSubscription(BaseActiveTimeStampModel):
    user_id = models.IntegerField(help_text='User id with a subscription')
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name='user_subscriptions')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    is_end_date_applicable = models.BooleanField(default=False)
    consumption = models.IntegerField(default=0)
    limited_consumption_valid = models.BooleanField(default=False)
    
    def __str__(self):
        return "{}-{}".format(self.user_id, self.subscription.name)
    
    


