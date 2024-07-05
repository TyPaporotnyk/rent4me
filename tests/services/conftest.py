import pytest

from core.apps.rentals.services.rentals import BaseRentalService, RentalService


@pytest.fixture
def rental_service() -> BaseRentalService:
    return RentalService()
