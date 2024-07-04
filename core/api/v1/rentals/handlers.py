from typing import List

from django.http import HttpRequest
from ninja import Router

from core.api.schemas import ApiResponse
from core.api.v1.rentals.schemas import RentalSchema
from core.apps.rentals.services.rentals import BaseRentalService
from core.config.containers import get_container

router = Router(tags=["Rentals"])


@router.get("/", response=ApiResponse[List[RentalSchema]])
def get_rental_list_handler(request: HttpRequest) -> ApiResponse[List[RentalSchema]]:
    container = get_container()
    rental_service: BaseRentalService = container.resolve(BaseRentalService)

    rental_list = rental_service.get_rental_list()

    items = [RentalSchema.from_entity(obj) for obj in rental_list]

    return ApiResponse(data=items)
