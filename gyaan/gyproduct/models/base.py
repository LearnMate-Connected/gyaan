from django.db import models

from django.utils import timezone

from _gybase.models.base import BaseActiveTimeStampModel

from gyproduct.constants import CATEGORY_CHOICES, OWNER_CHOICES, ELIGIBILITY_PARAM_CHOICES, SUBSCRIPTION_RESOURCE_CHOICES


class Category(BaseActiveTimeStampModel):
    """
    Args:
        BaseActiveTimeStampModel : Abstract models with necesary details for all models

    Returns:
        Category: We define category as universal classification of services on platform.
        Like: Online courses, Offline stocks for sale 
    """
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    icon = models.URLField(blank=True, null=True)
    custom_parameters = models.JSONField(default=dict, blank=True, null=True)
    created_by_id = models.PositiveBigIntegerField()
    updated_by_id = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return "{}-{}".format(self.name, self.active)


class Department(BaseActiveTimeStampModel):
    """
        Department: For every topic being published on platform there must be a department.
        Example : Topic Python will be of department IT. 
    """
    
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    help_email = models.EmailField(
        help_text="An email to support issues in these topics", blank=True, null=True)
    created_by_id = models.PositiveBigIntegerField()
    updated_by_id = models.PositiveBigIntegerField()
    min_age = models.IntegerField(blank=True, null=True)
    custom_parameters = models.JSONField(default=dict, blank=True, null=True)
    
    def __str__(self):
        return "{}".format(self.name)


class Topic(BaseActiveTimeStampModel):
    """
        Topic: For every Product or ProductGroup being published on platform there can be multiple topics.
        Example : Python courses that can be considered as a product/ product-group will be under Python topic. 
    """
    icon = models.URLField(blank=True, null=True, help_text="An image as an icon to the topic")
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    help_email = models.EmailField( blank=True, null=True, help_text="An email to support issues in these topics")
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='topics', blank=True, null=True)
    created_by_id = models.PositiveBigIntegerField()
    updated_by_id = models.PositiveBigIntegerField()
    custom_parameters = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)


class Eligibility(BaseActiveTimeStampModel):
    """
        Eligibility: We need to maintain some sort of restrictions on contents published on platform.
        As of now we don't know exactly the number of parameters for eligibility.
    """
    parameter = models.CharField(choices=ELIGIBILITY_PARAM_CHOICES)
    lower_limit = models.FloatField()
    upper_limit = models.FloatField()
    multiplier = models.FloatField(default=1.0)
    custom_parameters = models.JSONField(default=dict, blank=True, null=True)

    class Meta:
        unique_together = ('parameter', 'lower_limit', 'upper_limit')
    
    def __str__(self):
        return "{}-{}-{}".format(self.parameter,self.lower_limit, self.upper_limit)


class ProductGroup(BaseActiveTimeStampModel):
    """
        ProductGroup: All the products published together at a time will be under one product group.
        This must be sellable if active.
    """
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    icon = models.URLField(blank=True, null=True, help_text="An icon which can be thumbnail")
    created_by_id = models.CharField(max_length=10)
    updated_by_id = models.CharField(max_length=10)
    expiry_date = models.DateField(blank=True, null=True)
    is_expiry_enabled = models.BooleanField(default=False)
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    mrp = models.FloatField()
    owned_by = models.CharField(max_length=3, choices=OWNER_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, 
                                related_name='product_groups', 
                                help_text="A Product group must have a category"
                            )
    topic = models.ManyToManyField(Topic, related_name='product_groups')
    eligibility =  models.ManyToManyField(Eligibility, related_name='product_group')
    is_approved = models.BooleanField(default=False, help_text="It won't be true untill all products are approved in this group")
    approved_by_id = models.PositiveBigIntegerField()
    is_sellable = models.BooleanField(default=True)
    limited_consumption = models.BooleanField(default=False, help_text="If publisher wants to limit the consumption")
    consumption_quantity = models.FloatField(default=0.0, help_text="If limited consumption is applicable then there must be consumption quantity")
    limited_sale_applicable = models.BooleanField(default=False, help_text="If there are only limited quantity available for sale")
    quantity = models.FloatField(default=0.0, help_text="If limited sale applicable then there must be limited quanity")
    custom_parameters = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return "{}-{}-{}".format(self.name, self.selling_price, self.created_by_id)
    

class Product(BaseActiveTimeStampModel):
    """
        Product: All the products published under a product group.
        This can be sellable individually under a product group depending on publisher's choice.
    """
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    icon = models.URLField(blank=True, null=True)
    created_by_id = models.CharField(max_length=10)
    updated_by_id = models.CharField(max_length=10)
    product_group = models.ForeignKey(ProductGroup, on_delete=models.PROTECT, related_name='products', help_text="A product group created at time when products are published")
    eligibility = models.ManyToManyField(Eligibility, related_name='product')
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    mrp = models.FloatField()
    owned_by = models.CharField(max_length=3, choices=OWNER_CHOICES)
    approved_by_id = models.PositiveBigIntegerField()
    limited_consumption = models.BooleanField(default=False, help_text="If publisher wants to limit the consumption")
    consumption_quantity = models.FloatField(default=0.0, help_text="If limited consumption is applicable then there must be consumption quantity")
    is_sellable = models.BooleanField(default=False)
    limited_sale_applicable = models.BooleanField(default=False, help_text="If there are only limited quantity available for sale")
    quantity = models.FloatField(default=0.0, help_text="If limited sale applicable then there must be limited quanity")
    custom_parameters = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return "{}-{}-{}".format(self.name, self.product_group, self.created_by_id)


# TODO: Need to take a call whether we need to have a seperate django models for Resources and Contents
class ResourceContents(BaseActiveTimeStampModel):
    resource_type = models.CharField(choices=SUBSCRIPTION_RESOURCE_CHOICES)
    resource_id = models.IntegerField(help_text="Id of resource")
    video_content_link = models.URLField(blank=True, null=True)
    audio_content_link = models.URLField(blank=True, null=True)
    written_content_link = models.URLField(blank=True, null=True)
    image_content_link = models.URLField(blank=True, null=True)
    custom_parameters = models.JSONField(default=dict, blank=True, null=True)
    
    def __str__(self):
        return "{}-{}-{}".format(self.resource_type, self.resource_id, self.id)

