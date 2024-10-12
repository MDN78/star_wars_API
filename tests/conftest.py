import pytest
from common.apisession import TestSession
# from project_documents.customer import Customer


# @pytest.fixture
# def customer(scope='function') -> Customer:
#     return Customer.get_customer()


@pytest.fixture(scope='function')
def api_session():
    session = TestSession()
    session.base_url = 'https://swapi.dev/api'
    session.headers.update({'user-agent': 'Opera'})
    return session


@pytest.fixture(scope='session')
def api_wookie_session():
    session = TestSession()
    session.base_url = 'https://swapi.dev/api'
    session.headers.update({'user-agent': 'Opera'})
    session.params = {'format': 'wookie'}
    return session