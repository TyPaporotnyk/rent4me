import pytest

from core.apps.customers.services.customers import BaseCustomerService, ORMCustomerService
from core.apps.rentals.services.rentals import BaseRentalService, ORMRentalService


@pytest.fixture
def rental_service() -> BaseRentalService:
    return ORMRentalService()


@pytest.fixture
def customer_service() -> BaseCustomerService:
    return ORMCustomerService()
