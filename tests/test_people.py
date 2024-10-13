import pytest
import allure
from tests.conftest import api_session
from common.common import RESPONSE_BODY_404, RESPONSE_BODY_405
from models.people import People, ListPeople

# main_site = 'https://docs.spacexdata.com/'
# base_url = 'https://swapi.dev/api/'

@allure.feature('People')
class TestPeople:

    @allure.story('Positive tests')
    class TestPositive:

        @allure.title('Gett all people dates')
        def test_get_all_people(self, api_session):
            response = api_session.request(method='GET', path='/people/')
            print(response)
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            people = ListPeople.model_validate(response.json())
            # you can get some info from response in format json
            print(people.model_dump_json())

        @pytest.mark.skip('For allure statistic')
        def test_search_people(self, api_session):
            params = {'name': 'Ob-Wan Kenobi'}
            response = api_session.request(method='GET', path='/people/', params=params)
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            people = People.model_validate(response.json())
            assert people.name == 'Ob-Wan Kenobi'

        @allure.title('Gett first people date')
        def test_get_first_people(self, api_session):
            response = api_session.request(method='GET', path='/people/1/')
            assert response.status_code == 200
            resp = response.json()
            assert resp['name'] == 'Luke Skywalker'
            print(response.json())
            # validate by pandantic from directory models-people
            people = People.model_validate(resp)
            assert people.name == 'Luke Skywalker'

        @allure.title('Gett second people dates')
        def test_get_second_people(self, api_session):
            response = api_session.request(method='GET', path='/people/2/')
            assert response.status_code == 200
            resp = response.json()
            people = People.model_validate(resp)
            assert resp['name'] == 'C-3PO'
            assert people.name == 'C-3PO'
            people = People.model_validate(resp)
            assert people.name == 'C-3PO'

        @allure.title('Gett information about people without user agent')
        def test_get_without_header_user_agent(self, api_session):
            api_session.headers.pop('user-agent')
            response = api_session.request(method='GET', path='/people/')
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'

    @allure.story('Negative tests')
    class TestNegstive:

        def test_404(self, api_session):
            response = api_session.request(method='GET', path='/wrong/')
            print(response)
            assert response.status_code == 404
            assert response.headers.get('Content-Type') == 'text/html'

        def test_405(self, api_session):
            response = api_session.request(method='POST', path='/people/2/')
            assert response.status_code == 405
            assert response.text == RESPONSE_BODY_405
            assert response.json() == {"detail":"Method 'POST' not allowed."}

        def test_wrong_query(self, api_session):
            response = api_session.request(method='GET', path='/people/abcd')
            assert response.status_code == 404
            assert response.text == RESPONSE_BODY_404
