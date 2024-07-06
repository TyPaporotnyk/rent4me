from django.contrib import admin

from core.apps.customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("username",)
    readonly_fields = ("token",)
