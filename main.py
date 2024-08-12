from src.hh_api import HeadHunter
from src.json_saver import JsonSaver
from src.user_vacancies import sorting


def user_interface():

    """Функция для взаимодействия с пользователем"""

    print("Добро пожаловать на платформу HeadHunter")
    name_vac = input('Введите название вакансии: \n')
    hh = HeadHunter()
    json_saver = JsonSaver()
    vacancies = hh.get_vacancies(name_vac)
    json_saver.save_vacancies(vacancies)
    name_criterion = input('Введите критерий для отбора вакансий: \n')
    json_saver.get_data(name_criterion)
    n = input('Введите количество вакансий для просмотра: \n')
    sorting(int(n))
    name_exit = input('Завершим и очистим файл вакансий да/нет : \n')
    if name_exit == 'да':
        json_saver.delete_vacancy()
    else:
        user_interface()


if __name__ == "__main__":
    user_interface()
