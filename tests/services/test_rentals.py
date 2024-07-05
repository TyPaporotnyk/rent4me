import pytest

from core.apps.rentals.exceptions.rentals import RentalNotFound
from core.apps.rentals.services.rentals import BaseRentalService
from tests.factories.rentals import RentalModelFactory


@pytest.mark.django_db
def test_get_all_rentals(rental_service: BaseRentalService):
    expected_count = 5
    rentals = RentalModelFactory.create_batch(size=expected_count)
    rentals_titles = {rental.title for rental in rentals}

    fetched_rentals = rental_service.get_rental_list()
    fetched_titles = {rental.title for rental in fetched_rentals}

    assert len(fetched_titles) == expected_count, f"{fetched_titles=}"
    assert rentals_titles == fetched_titles, f"{rentals_titles=}"


@pytest.mark.django_db
def test_get_rental_by_id(rental_service: BaseRentalService):
    rental = RentalModelFactory.create()

    fetched_rental = rental_service.get_by_id(rental_id=rental.id)

    assert rental.title == fetched_rental.title, f"{fetched_rental=}"


@pytest.mark.django_db
def test_get_rental_by_id_not_found(rental_service: BaseRentalService):
    with pytest.raises(RentalNotFound):
        rental_service.get_by_id(rental_id=-1)
