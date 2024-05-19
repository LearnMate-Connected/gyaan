from django.contrib import admin
from gyproduct.models.base import (
Category, Department, Topic,  Eligibility, ProductGroup, Product)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'id', 'active')
    list_filter = ('name', 'active', 'id')
    search_fields = ('name', 'active', 'id')
    date_hierarchy = 'updated_at'
    

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'min_age', 'description')
    list_filter = ('name', 'min_age')
    search_fields = ('name', 'min_age', 'id')
    date_hierarchy = 'updated_at'
    

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'department')

    list_filter = ('name', 'department__name')

    search_fields = ('name', 'department__name', 'id')
    date_hierarchy = 'updated_at'


@admin.register(Eligibility)
class EligibilityAdmin(admin.ModelAdmin):
    list_display = ('parameter', 'lower_limit', 'upper_limit')
    list_filter = ('parameter', 'lower_limit', 'upper_limit')
    search_fields = ('parameter', 'lower_limit', 'upper_limit')
    date_hierarchy = 'updated_at'


@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    def category_name(self, obj):
        return obj.category.name
    
    list_display = ('name', 'created_by_id', 'cost_price', 'selling_price', 'owned_by', 'category_name')
    list_filter = ('name', 'created_by_id', 'cost_price', 'selling_price', 'owned_by', 'category')
    search_fields = ('name', 'created_by_id', 'cost_price', 'selling_price', 'owned_by', 'category_name')
    date_hierarchy = 'updated_at'
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def group_name(self, obj):
        return obj.product_group.name
    
    list_display = ('name', 'created_by_id', 'cost_price', 'selling_price', 'owned_by', 'group_name')
    list_filter = ('name', 'created_by_id', 'cost_price', 'selling_price', 'owned_by', 'product_group')
    search_fields = ('name', 'created_by_id', 'cost_price', 'selling_price', 'owned_by', 'group_name')
    date_hierarchy = 'updated_at'