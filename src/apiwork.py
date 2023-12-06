# https://vc.ru/u/1510590-python-idea/688002-parser-hh-veb-prilozhenie-na-python


import json
from abc import abstractmethod
import time
from os import getenv
from datetime import datetime
from vacancy import Vacancy
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
    def select_api():
        user_input = int(input("Если вы хотите получить вакансии с сайта hh.ru"
                               " введите \033[36m0\n"
                               "\033[0mЕсли вы хотите получить вакансии с сайта"
                               "superjob.ru нажмите \033[36m1\n\033[0m>> "))

        if user_input == 0:
            print("\nВы предпочли вакансии с сайта \033[92mhh.ru")
            searching_word = input("\033[0mВведите ключевое слова или фразу"
                                   " искомой вакансии:\n>> ")
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))

            hh = HeadHunterAPI().get_vacancies(searching_word, top_n)
            return hh

        elif user_input == 1:
            print("\nВы предпочли вакансии с сайта \033[92msuperjob.ru")
            searching_word = input("\033[0mВведите ключевое слова или фразу"
                                   " искомой вакансии:\n>> ")
            top_n = int(input("Введите количество вакансий для вывода в топ N: "))
            super_job = SuperjobAPI().get_vacancies(searching_word, top_n)
            return super_job
        else:
            print("\nНекорректное значение, повторить ввод ?\ny/n")
            return None


class HeadHunterAPI(ApiWork):
    url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, searching_word, top_n):

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


            # for searching_word in vacancies:
            #     # Extract relevant information from the searching_word object
            #     vacancy_id = searching_word.get("id")
            #     vacancy_title = searching_word.get("name")
            #     vacancy_url = searching_word.get("alternate_url")
            #     company_name = searching_word.get("employer", {}).get("name")
            #     print(f"ID: {vacancy_id}\nTitle: {vacancy_title}\nCompany:"
            #           f" {company_name}\nURL: {vacancy_url}\n")
        else:
            print(f"Request failed with status code: {response.status_code}")


class SuperjobAPI(ApiWork):
    # def __init__(self, name, page, top_n):
    #     self.name = name
    #     self.page = page
    #     self.top_n = top_n
    #     self.url = 'https://api.superjob.ru/2.0/vacancies/'

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
            print(data['objects'][0])
            print(data['objects'][1])
            return data
        except ConnectionError:
            print("Что-то не так с сетевым подключением")

    def load_vacancy(self):
        """Проходим циклом по словарю берем из словаря
        только нужные нам данные и записываем их
        в переменную 'vacancy_list_SJ' """
        data = self.get_vacancies()
        vacancy_list_SJ = []
        for i in data['objects']:
            published_at = datetime.fromtimestamp(i.get('date_published', ''))
            super_job = {
                'id': i['id'],
                'name': i.get('profession', ''),
                'solary_ot': i.get('payment_from', '') if i.get('payment_from') else None,
                'solary_do': i.get('payment_to') if i.get('payment_to') else None,
                'responsibility': i.get('candidat').replace('\n', '').replace('•', '') if i.get('candidat') else None,
                'data': published_at.strftime("%d.%m.%Y"),

            }
            vacancy_list_SJ.append(super_job)

        print(vacancy_list_SJ)
        return vacancy_list_SJ


ApiWork.select_api()
