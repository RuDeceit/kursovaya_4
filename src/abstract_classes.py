from abc import ABC, abstractmethod


class Api(ABC):

    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass


class AbstractJson(ABC):

    """Абстрактный класс для работы с json файлом"""

    @abstractmethod
    def save_vacancies(self, *args):
        pass

    @abstractmethod
    def get_data(self, *args):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass
