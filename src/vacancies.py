class Vacancy:

    """Класс для работы с вакансиями"""

    def __init__(self, name, salary, url, responsibility, requirement='Информация отсутствует'):
        self.name = name
        self.salary = salary if salary else "Не указано"
        self.url = url
        self.responsibility = responsibility
        self.requirement = requirement

    def validate_salary(self):
        if self.salary == 0:
            self.salary = 'Зарплата не указана'
            return self.salary

    def __repr__(self):

        """Строковое представление объекта класса Vacancy"""

        return (f'Название вакансии: {self.name}\n'
                f'Зарплата: {self.salary}\n'
                f'Описание: {self.responsibility}\n'
                f'Требования: {self.requirement}\n'
                f'Ссылка на вакансию: <{self.url}>\n')

    def __gt__(self, other):

        """Метод сравнения вакансий между собой по зарплате и валидации данных по зарплате"""

        if self.salary is not None and other.salary is not None:
            if self.salary['to'] > other.salary['to']:
                return self
            else:
                return other
        return 'Зарплата не указана'

    def __lt__(self, other):

        """Метод сравнения вакансий между собой по зарплате и валидации данных по зарплате"""

        if self.salary is not None and other.salary is not None:
            if self.salary['to'] < other.salary['to']:
                return self
            else:
                return other
        return 'Зарплата не указана'
