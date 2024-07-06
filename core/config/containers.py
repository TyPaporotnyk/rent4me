from functools import lru_cache
from logging import Logger, getLogger

import punq

from core.apps.rentals.services.rentals import BaseRentalService, ORMRentalService


@lru_cache(1)
def get_container() -> punq.Container:
    return _initialize_container()


def _initialize_container() -> punq.Container:
    container = punq.Container()

    # init internal stuff
    container.register(Logger, factory=getLogger, name="django.request")

    # initialize services
    container.register(BaseRentalService, ORMRentalService)

    return container
