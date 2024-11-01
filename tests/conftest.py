import allure
import pytest
from common.apisession import TestSession


@allure.step("Create session")
@pytest.fixture(scope='function')
def api_session():
    session = TestSession()
    session.base_url = 'https://swapi.dev/api'
    session.headers.update({'user-agent': 'Opera'})
    return session


@allure.step("Create wookie sesssion")
@pytest.fixture(scope='session')
def api_wookie_session():
    session = TestSession()
    session.base_url = 'https://swapi.dev/api'
    session.headers.update({'user-agent': 'Opera'})
    session.params = {'format': 'wookie'}
    return session
