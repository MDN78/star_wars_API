import pytest
import allure
from tests.conftest import api_session
from common.common import RESPONSE_BODY_404, RESPONSE_BODY_405
from models.films import Films, ListFilms


class TestFilms:
    class TestPositive:
        def test_get_all_films(self, api_session):
            response = api_session.request(method='GET', path='/films/')
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            films = ListFilms.model_validate(response.json())

        def test_get_first_film(self, api_session):
            response = api_session.request(method='GET', path='/films/1/')
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            resp = response.json()
            film = Films.model_validate(resp)
            assert resp['title'] == 'A New Hope'

    class TestNegative:
        def test_404(self, api_session):
            response = api_session.request(method='GET', path='/films/a/')
            assert response.status_code == 404
            assert response.headers.get('Content-Type') == 'application/json'
