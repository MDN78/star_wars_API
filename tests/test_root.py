import allure
from models.root import Root
from tests.conftest import api_session


@allure.feature('Root')
class TestRoot:
    @allure.story('Positive tests')
    class TestPositive:

        @allure.title('Gett all roots')
        def test_get_all_roots(self, api_session):
            response = api_session.request(method='GET', path='/')
            with allure.step('Status code = 200'):
                assert response.status_code == 200
            with allure.step('Check content type'):
                assert response.headers.get('content-type') == 'application/json'
            with allure.step('Validate response json'):
                Root.model_validate(response.json())

    @allure.story('Negative tests')
    class TestNegative:

        @allure.title('Get bad request')
        def test_404(self, api_session):
            response = api_session.request(method='GET', path='/wrong/')
            with allure.step('Status code = 404'):
                assert response.status_code == 404
            with allure.step('Response headers'):
                assert response.headers.get('Content-Type') == 'text/html'
