import factory
from factory.django import DjangoModelFactory

from core.apps.rentals.models import Rental


class RentalModelFactory(DjangoModelFactory):
    title = factory.Faker("first_name")
    description = factory.Faker("text")

    class Meta:
        model = Rental
