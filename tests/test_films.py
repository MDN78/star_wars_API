import allure
from tests.conftest import api_session
from models.films import Films, ListFilms
from common.common import RESPONSE_BODY_404, RESPONSE_BODY_405


@allure.feature('Films')
class TestFilms:
    @allure.story('Positive tests')
    class TestPositive:

        @allure.title('Gett all films')
        def test_get_all_films(self, api_session):
            response = api_session.request(method='GET', path='/films/')
            with allure.step('Status code = 200'):
                assert response.status_code == 200
            with allure.step('Content type'):
                assert response.headers.get('content-type') == 'application/json'
            with allure.step('JSON validate'):
                films = ListFilms.model_validate(response.json())

        @allure.title('Gett first film')
        def test_get_first_film(self, api_session):
            response = api_session.request(method='GET', path='/films/1/')

            with allure.step('Status code = 200'):
                assert response.status_code == 200
            with allure.step('Content type'):
                assert response.headers.get('content-type') == 'application/json'

            with allure.step('Validate title'):
                resp = response.json()
                film = Films.model_validate(resp)
                assert resp['title'] == 'A New Hope'

    @allure.story('Negative tests')
    class TestNegative:

        @allure.title('Get 404')
        def test_404(self, api_session):
            response = api_session.request(method='GET', path='/films/a/')
            with allure.step('Status code = 404'):
                assert response.status_code == 404
            with allure.step('Response headers'):
                assert response.headers.get('Content-Type') == 'application/json'

        @allure.title('Wrong query')
        def test_wrong_query(self, api_session):
            response = api_session.request(method='GET', path='/films/abcd/')
            with allure.step('Status code = 404'):
                assert response.status_code == 404
            with allure.step('Response body = 404'):
                assert response.text == RESPONSE_BODY_404

        @allure.title('Get 405')
        def test_405(self, api_session):
            response = api_session.request(method='POST', path='/films/')
            with allure.step('Status code = 405'):
                assert response.status_code == 405
            with allure.step('Response body = 405'):
                assert response.text == RESPONSE_BODY_405
            with allure.step('Method POST not allowed'):
                assert response.json() == {"detail": "Method 'POST' not allowed."}
