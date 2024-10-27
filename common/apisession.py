import os
import logging
import datetime
from utils import resource
from requests import Session, Response


def write_log_to_file(data: str):
    log_file = 'LOG_FILE'
    # log_file = os.getenv('LOG_FILE')
    file_name = (resource.path_log_file(log_file) + ".log")
    with open(file_name, 'a', encoding='utf=8') as logger_file:
        logger_file.write(data + '\n')


''' Добавим функцию которая будет автоматически цеплять логи'''

logger = logging.getLogger()


def allure_request_logger(function):
    def wrapper(*args, **kwargs):
        response: Response = function(*args, **kwargs)
        method = response.request.method
        url = response.request.url
        logger.info(method)
        url = logger.info(url)
        logger.info(response.request.headers)
        logger.info(response.request.body)
        logger.info(response.headers)
        try:
            logger.info(response.json())
        except ValueError:
            print('Response without JSON')
        return response

    return wrapper


'''Переопределили класс session под свои нужды и задали там параметры'''


class TestSession(Session):
    # чтобы не выскакивала ошибка тк в классе с названием Тест нет по факту тестов или переименовывать класс
    __test__ = False

    def __init__(self):
        # инициализатор session в классе
        super().__init__()
        self.base_url = None
        # self.base_url = base_url

    @allure_request_logger
    def request(self, path, method='GET'):
        joined_url = f'{self.base_url}{path}'
        write_log_to_file(
            f"\n-----\n"
            + f"Start time: {str(datetime.datetime.now())}\n"
            + '\n'
            + f'Method: {method}'
            + '\n'
            + f'Url: {joined_url}'
        )
        return super().request(method, joined_url)

# , *args, **kwargs
