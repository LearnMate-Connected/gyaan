
from django.contrib import admin

from gyuser.models import User, Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'first_name', 'is_staff', 'is_active')

    list_filter = ('email', 'username', 'is_staff', 'is_active')

    search_fields = ('email', 'username')
    date_hierarchy = 'date_joined'



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'city', 'is_working', 'user')

    list_filter = ('user', 'phone', 'city', 'is_working')

    search_fields = ('email', 'phone')
    date_hierarchy = 'updated_at'
