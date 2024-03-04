# from django.contrib.postgres.fields import JSONField
from django.db import models

from django.utils import timezone

from _gybase.models.base import BaseActiveTimeStampModel

from gyproduct.constants import CATEGORY_CHOICES, OWNER_CHOICES, ELIGIBILITY_PARAM_CHOICES


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
    created_by_id = models.CharField(max_length=10)
    updated_by_id = models.CharField(max_length=10)

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
    created_by_id = models.CharField(max_length=10)
    updated_by_id = models.CharField(max_length=10)
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
    created_by_id = models.CharField(max_length=10)
    updated_by_id = models.CharField(max_length=10)
    custom_parameters = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.name)

class Eligibility(BaseActiveTimeStampModel):
    """
        Eligibility: We need to maintain some sort of restrictions on contents published on platform.
        As of now we don't know exactly the number of parameters for eligibility.
    """
    parameter = models.CharField(choices=ELIGIBILITY_PARAM_CHOICES)
    lower_limit = models.IntegerField()
    upper_limit = models.IntegerField()
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
    icon = models.URLField(max_length=200, blank=True, null=True)
    cost_price = models.PositiveBigIntegerField()
    selling_price = models.PositiveBigIntegerField()
    owned_by = models.CharField(max_length=3, choices=OWNER_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, 
                                related_name='product_groups', 
                                help_text="A Product group must have a category"
                            )
    topic = models.ManyToManyField(Topic, related_name='product_groups')
    created_by_id = models.CharField(max_length=10)
    updated_by_id = models.CharField(max_length=10)
    eligibility =  models.ForeignKey(Eligibility, on_delete=models.PROTECT, related_name='product_group')
    is_approved = models.BooleanField(default=False, help_text="It won't be true untill all products are approved in this group")
    approved_by_id = models.CharField(max_length=10)
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
    eligibility = models.ForeignKey(Eligibility, on_delete=models.PROTECT, related_name='product', blank=True, null=True)
    cost_price = models.PositiveBigIntegerField()
    selling_price = models.PositiveBigIntegerField()
    owned_by = models.CharField(max_length=3, choices=OWNER_CHOICES)
    approved_by_id = models.CharField(max_length=10)
    limited_consumption = models.BooleanField(default=False, help_text="If publisher wants to limit the consumption")
    consumption_quantity = models.FloatField(default=0.0, help_text="If limited consumption is applicable then there must be consumption quantity")
    is_sellable = models.BooleanField(default=False)
    limited_sale_applicable = models.BooleanField(default=False, help_text="If there are only limited quantity available for sale")
    quantity = models.FloatField(default=0.0, help_text="If limited sale applicable then there must be limited quanity")
    custom_parameters = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return "{}-{}-{}".format(self.name, self.product_group, self.created_by_id)

