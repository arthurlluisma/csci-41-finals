from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Customer

class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [CustomerInline,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Customer)
