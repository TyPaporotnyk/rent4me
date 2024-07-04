from abc import ABC, abstractmethod
from typing import Iterable

from core.apps.rentals.entities import Rental
from core.apps.rentals.models import Rental as RentalModel


class BaseRentalService(ABC):

    @abstractmethod
    def get_rental_list(self) -> Iterable[Rental]: ...


class RentalService(BaseRentalService):

    def get_rental_list(self) -> Iterable[Rental]:
        qs = RentalModel.objects.all()

        return [rental.to_entity() for rental in qs]
