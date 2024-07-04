from ninja import Router

from core.api.v1.rentals.handlers import router as rental_router

router = Router(tags=["v1"])

router.add_router("rentals/", rental_router)
