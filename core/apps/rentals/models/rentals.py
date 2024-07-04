from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.rentals.entities import Rental as RentalEntity


class Rental(TimedBaseModel):
    title = models.CharField(max_length=255, verbose_name="Rental title")
    description = models.TextField(blank=True, verbose_name="Rental description")
    is_active = models.BooleanField(default=True, verbose_name="Is rental active")

    def to_entity(self) -> RentalEntity:
        return RentalEntity(
            id=self.id,
            title=self.title,
            description=self.description,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Rental"
        verbose_name_plural = "Rentals"
