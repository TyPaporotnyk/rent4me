from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class RentalNotFound(ServiceException):
    rental_id: int

    @property
    def message(self):
        return "Rental not found"
