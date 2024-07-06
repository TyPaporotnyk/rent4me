from abc import ABC, abstractmethod
from uuid import uuid4

from core.apps.customers.entities import Customer
from core.apps.customers.exceptions.customers import CustomerNotFound, CustomerTokenNotValid
from core.apps.customers.models import Customer as CustomerModel


class BaseCustomerService(ABC):

    @abstractmethod
    def get_or_create(self, username: str) -> Customer: ...

    @abstractmethod
    def generate_token(self, customer: Customer) -> str: ...

    @abstractmethod
    def get(self, username: str) -> Customer: ...

    @abstractmethod
    def get_by_token(self, token: str) -> Customer: ...


class ORMCustomerService(BaseCustomerService):

    def get_or_create(self, username: str) -> Customer:
        customer_dto, _ = CustomerModel.objects.get_or_create(username=username)
        return customer_dto.to_entity()

    def generate_token(self, customer: Customer) -> str:
        new_token = str(uuid4())
        CustomerModel.objects.filter(username=customer.username).update(token=new_token)

        return new_token

    def get(self, username: str) -> Customer:
        try:
            customer_dto = CustomerModel.objects.get(username=username)
        except CustomerModel.DoesNotExist:
            raise CustomerNotFound(username=username)

        return customer_dto.to_entity()

    def get_by_token(self, token: str) -> Customer:
        try:
            customer_dto = CustomerModel.objects.get(token=token)
        except CustomerModel.DoesNotExist:
            raise CustomerTokenNotValid(token=token)

        return customer_dto.to_entity()
