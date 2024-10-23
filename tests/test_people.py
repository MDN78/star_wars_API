import pytest
import allure
from tests.conftest import api_session
from models.people import People, ListPeople
from common.common import RESPONSE_BODY_404, RESPONSE_BODY_405


@allure.feature('People')
class TestPeople:
    @allure.story('Positive tests')
    class TestPositive:

        @allure.title('Gett all people dates')
        def test_get_all_people(self, api_session):
            response = api_session.request(method='GET', path='/people/')
            with allure.step('Status code = 200'):
                assert response.status_code == 200
            with allure.step('Check content type'):
                assert response.headers.get('content-type') == 'application/json'
            with allure.step('Validate response json'):
                people = ListPeople.model_validate(response.json())
            # you can get some info from response in format json
            # print(people.model_dump_json())

        @pytest.mark.skip('Close for update')
        def test_search_people(self, api_session):
            params = {'name': 'Ob-Wan Kenobi'}
            response = api_session.request(method='GET', path='/people/', params=params)
            with allure.step('Status code = 200'):
                assert response.status_code == 200
            with allure.step('Check content type'):
                assert response.headers.get('content-type') == 'application/json'
            people = People.model_validate(response.json())
            with allure.step(f'Check name {people.name}'):
                assert people.name == 'Ob-Wan Kenobi'

        @allure.title('Gett first people date')
        def test_get_first_people(self, api_session):
            response = api_session.request(method='GET', path='/people/1/')
            resp = response.json()
            people = People.model_validate(resp)

            with allure.step('Status code = 200'):
                assert response.status_code == 200

            with allure.step(f'Check name from response {resp['name']}'):
                assert resp['name'] == 'Luke Skywalker'
            # validate by pandantic from directory models-people
            with allure.step(f'Check name {people.name}'):
                assert people.name == 'Luke Skywalker'

        @allure.title('Gett second people dates')
        def test_get_second_people(self, api_session):
            response = api_session.request(method='GET', path='/people/2/')
            resp = response.json()
            people = People.model_validate(resp)

            with allure.step('Status code = 200'):
                assert response.status_code == 200
            with allure.step('Check name from response scheme'):
                assert resp['name'] == 'C-3PO'
            with allure.step('Check name'):
                assert people.name == 'C-3PO'


        @allure.title('Get information about people without user agent')
        def test_get_without_header_user_agent(self, api_session):
            api_session.headers.pop('user-agent')
            response = api_session.request(method='GET', path='/people/')
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'

    @allure.story('Negative tests')
    class TestNegstive:

        @allure.title('Get 404')
        def test_404(self, api_session):
            response = api_session.request(method='GET', path='/wrong/')
            assert response.status_code == 404
            assert response.headers.get('Content-Type') == 'text/html'

        @allure.title('Get 405')
        def test_405(self, api_session):
            response = api_session.request(method='POST', path='/people/2/')
            assert response.status_code == 405
            assert response.text == RESPONSE_BODY_405
            assert response.json() == {"detail": "Method 'POST' not allowed."}

        @allure.title('Wrong query')
        def test_wrong_query(self, api_session):
            response = api_session.request(method='GET', path='/people/abcd')
            assert response.status_code == 404
            assert response.text == RESPONSE_BODY_404
