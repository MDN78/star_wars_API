import logging
from requests import Session, Response

''' Добавим функцию которая будет автоматически цеплять логи'''

logger = logging.getLogger()


def allure_request_logger(function):
    def wrapper(*args, **kwargs):
        response: Response = function(*args, **kwargs)
        method = response.request.method
        url = response.request.url
        logger.info(method)
        logger.info(url)
        logger.info(response.request.headers)
        logger.info(response.request.body)
        logger.info(response.headers)
        logger.info(response.json())
        return response

    return wrapper


'''Переопределили класс session под свои нужды и задали там параметры'''


class TestSession(Session):
    # чтобы не выскакивала ошибка тк в классе с названием Тест нет по факту тестов или переименовывать класс
    __test__ = False

    def __init__(self):
        # инициализатор session в классе
        super().__init__()
        # self.base_url = base_url

    @allure_request_logger
    def request(self, path, method='GET', *args, **kwargs):
        joined_url = f'{self.base_url}{path}'
        return super().request(method, joined_url, *args, **kwargs)
