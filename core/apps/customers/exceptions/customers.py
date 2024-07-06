from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class CustomerNotFound(ServiceException):
    username: str

    @property
    def message(self) -> str:
        return "Customer does not exist"


@dataclass(eq=False)
class CustomerTokenNotValid(ServiceException):
    token: str

    @property
    def message(self) -> str:
        return "Customer does not exist with provided token"
