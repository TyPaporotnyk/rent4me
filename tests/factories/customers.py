import factory
from factory.django import DjangoModelFactory

from core.apps.customers.models import Customer


class CustomerModelFactory(DjangoModelFactory):
    username = factory.Faker("first_name")

    class Meta:
        model = Customer
