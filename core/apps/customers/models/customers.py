from uuid import uuid4

from django.db import models

from core.apps.common.models import TimedBaseModel
from core.apps.customers.entities import Customer as CustomerEntity


class Customer(TimedBaseModel):
    username = models.CharField(max_length=255, unique=True, verbose_name="Customer username")
    token = models.CharField(max_length=255, default=uuid4, unique=True, verbose_name="Customer token")

    def to_entity(self) -> CustomerEntity:
        return CustomerEntity(
            id=self.id,
            username=self.username,
            created_at=self.created_at,
        )

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
