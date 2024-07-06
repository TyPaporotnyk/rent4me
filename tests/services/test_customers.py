import pytest
from faker import Faker

from core.apps.customers.exceptions.customers import CustomerNotFound, CustomerTokenNotValid
from core.apps.customers.models.customers import Customer as CustomerModel
from core.apps.customers.services.customers import BaseCustomerService
from tests.factories.customers import CustomerModelFactory


@pytest.mark.django_db
def test_get_or_create_customer(customer_service: BaseCustomerService):
    fake = Faker()
    customer_username = fake.name()

    created_customer = customer_service.get_or_create(username=customer_username)
    fetched_customer = customer_service.get_or_create(username=customer_username)

    assert customer_username == created_customer.username, f"{created_customer=}"
    assert customer_username == fetched_customer.username, f"{fetched_customer=}"


@pytest.mark.django_db
def test_get_by_username_customer(customer_service: BaseCustomerService):
    customer = CustomerModelFactory.create()

    fetched_customer = customer_service.get(username=customer.username)

    assert customer.username == fetched_customer.username, f"{fetched_customer=}"


@pytest.mark.django_db
def test_get_by_username_customer_not_found(customer_service: BaseCustomerService):
    with pytest.raises(CustomerNotFound):
        customer_service.get(username="not_valid_username")


@pytest.mark.django_db
def test_get_by_token_customer(customer_service: BaseCustomerService):
    customer = CustomerModelFactory.create()

    fetched_customer = customer_service.get_by_token(token=customer.token)

    assert customer.username == fetched_customer.username, f"{fetched_customer=}"


@pytest.mark.django_db
def test_get_by_token_customer_not_found(customer_service: BaseCustomerService):
    with pytest.raises(CustomerTokenNotValid):
        customer_service.get_by_token(token="not_valid_token")


@pytest.mark.django_db
def test_generate_token_for_customer(customer_service: BaseCustomerService):
    customer = CustomerModelFactory.create()

    customer_item = customer.to_entity()

    new_customer_token = customer_service.generate_token(customer=customer_item)
    fetched_customer = CustomerModel.objects.get(id=customer_item.id)

    assert fetched_customer.token == new_customer_token, f"{fetched_customer=}"
