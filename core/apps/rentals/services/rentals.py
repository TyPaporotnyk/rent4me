from abc import ABC, abstractmethod
from typing import Iterable

from core.apps.rentals.entities import Rental
from core.apps.rentals.exceptions.rentals import RentalNotFound
from core.apps.rentals.models import Rental as RentalModel


class BaseRentalService(ABC):

    @abstractmethod
    def get_rental_list(self) -> Iterable[Rental]: ...

    @abstractmethod
    def get_by_id(self, rental_id: int) -> Rental: ...


class ORMRentalService(BaseRentalService):

    def get_rental_list(self) -> Iterable[Rental]:
        qs = RentalModel.objects.all()

        return [rental.to_entity() for rental in qs]

    def get_by_id(self, rental_id: int) -> Rental:
        try:
            rental_dto = RentalModel.objects.get(pk=rental_id)
        except RentalModel.DoesNotExist:
            raise RentalNotFound(rental_id=rental_id)

        return rental_dto.to_entity()
