from django.contrib import admin

from core.apps.rentals.models import Rental


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at", "is_active")
