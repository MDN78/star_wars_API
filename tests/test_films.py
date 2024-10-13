import pytest
import allure
from tests.conftest import api_session
from common.common import RESPONSE_BODY_404, RESPONSE_BODY_405
from models.films import Films, ListFilms


class TestFilms:

    class TestPositive:
        def test_get_all_films(self, api_session):
            response = api_session.request(method='GET', path='/films/')
            print(response)
            assert response.status_code == 200
            assert response.headers.get('content-type') == 'application/json'
            films = ListFilms.model_validate(response.json())
            # starships = ListStarships.model_validate(response.json())