import pytest
import allure
from models.starships import ListStarships, Starships
from common.common import RESPONSE_BODY_404, RESPONSE_BODY_405
from tests.conftest import api_session

base_url = 'https://swapi.dev/api/'

@allure.feature('Starships')
class TestStarships:

    @allure.story('Positive tests')
    class TestPositive:

        def test_get_all_starships(self, api_session):
            response = api_session.request(method='GET', path='/starships/')
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            starships = ListStarships.model_validate(response.json())

        @pytest.mark.skip('For allure statistic')
        def test_search_starship(self, api_session):
            params = {'name': 'X-wing'}
            response = api_session.request(method='GET', path='/starships/', params=params)
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            starship = Starships.model_validate(response.json())
            assert starship.name == 'X-wing'

        def test_get_ninth_starship(self, api_session):
            response = api_session.request(method='GET', path='/starships/9/')
            assert response.status_code == 200
            assert response.json()['name'] == 'Death Star'
            assert response.headers.get('content-type') == 'application/json'
            starship = Starships.model_validate(response.json())
            assert starship.name == 'Death Star'

        def test_get_second_starship(self, api_session):
            response = api_session.request(method='GET', path='/starships/2/')
            assert response.status_code == 200
            assert response.json()['name'] == 'CR90 corvette'
            assert response.headers.get('content-type') == 'application/json'
            starship = Starships.model_validate(response.json())
            assert starship.name == 'CR90 corvette'

    @allure.story('Negative tests')
    class TestNegstive:

        def test_404(self, api_session):
            response = api_session.request(method='GET', path='/wrong/')
            assert response.status_code == 404
            assert response.headers.get('Content-Type') == 'text/html'

        def test_405(self, api_session):
            response = api_session.request(method='POST', path='/starships/2/')
            assert response.status_code == 405
            assert response.text == RESPONSE_BODY_405
            # assert response.json() == {"detail":"Method 'POST' not allowed."}

        def test_wrong_query(self, api_session):
            response = api_session.request(method='GET', path='/starships/abcd')
            assert response.status_code == 404
            assert response.text == RESPONSE_BODY_404