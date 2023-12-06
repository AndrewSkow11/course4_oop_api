from os import getenv
from datetime import datetime
from abc import ABC, abstractmethod
import requests


# 1
# Создать абстрактный класс для работы с API сайтов с вакансиями.
# Реализовать классы, наследующиеся от абстрактного класса,
# для работы с конкретными платформами.
# Классы должны уметь подключаться к API и получать вакансии.


class ApiWork(ABC):
    def __init__(self):
        print("\033[33mConnecting to API ...\033[0m")

    @abstractmethod
    def get_vacancies(self, word, top_n):
        pass


    @staticmethod
    def set_arguments_for_api(number_for_site):
        sites = ['hh.ru', 'superjob.ru']

        print(f"\nВы предпочли вакансии с сайта "
              f"\033[92m{sites[number_for_site]}")
        searching_word = input("\033[0mВведите ключевое слова или фразу"
                               " искомой вакансии:\n>> ")
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        return searching_word, top_n

    @staticmethod
    def select_api():
        user_input = int(input("Если вы хотите получить вакансии с сайта hh.ru"
                               " введите \033[36m0\n"
                               "\033[0mЕсли вы хотите получить вакансии с сайта"
                               "superjob.ru нажмите \033[36m1\n\033[0m>> "))

        if user_input == 0:
            arguments = ApiWork.set_arguments_for_api(0)
            hh = HeadHunterAPI().get_vacancies(arguments[0], arguments[1])
            return hh

        elif user_input == 1:
            arguments = ApiWork.set_arguments_for_api(1)
            super_job = SuperjobAPI().get_vacancies(arguments[0], arguments[1])
            return super_job
        else:
            print("\nНекорректное значение, повторить ввод ?\ny/n")
            return None


class HeadHunterAPI(ApiWork):
    """Поле класса - базовый URL"""
    url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, searching_word, top_n):
        """Возвращает список вакансий по искомому слову
        в соответствии с введённым количеством"""

        params = {
            "text": searching_word,
            "per_page": top_n,  # Number of vacancies per page
        }

        response = requests.get(self.url, params=params)

        if response.status_code == 200:
            data = response.json()
            vacancies = data.get("items", [])

            print(vacancies)
            return vacancies
        else:
            print(f"Request failed with status code: {response.status_code}")


class SuperjobAPI(ApiWork):

    def get_vacancies(self, searching_word, top_n):

        url = 'https://api.superjob.ru/2.0/vacancies/'

        headers = {
            'X-Api-App-Id': getenv('API_KEY_SJ'),
        }

        try:
            data = requests.get(url, headers=headers,
                                params={'keywords': searching_word,
                                        'page': 0,
                                        'count': top_n}).json()
            print(data['objects'])
            return data
        except ConnectionError:
            print("Что-то не так с сетевым подключением")


ApiWork.select_api()
