# https://vc.ru/u/1510590-python-idea/688002-parser-hh-veb-prilozhenie-na-python


import json
from abc import abstractmethod
import time
from datetime import datetime
from vacancy import Vacancy
from abc import ABC, abstractmethod
import requests


# 1
# Создать абстрактный класс для работы с API сайтов с вакансиями.
# Реализовать классы, наследующиеся от абстрактного класса,
# для работы с конкретными платформами.
# Классы должны уметь подключаться к API и получать вакансии.


# Платформы для сбора вакансий
#  hh.ru (ссылка на API: https://github.com/hhru/api)
#  superjob.ru (ссылка на API: https://api.superjob.ru/)

# Прежде чем начать использовать API от SuperJob, необходимо зарегистрироваться
# (https://www.superjob.ru/auth/login/)
# и получить токен для работы.
# Подробная инструкция дается по ссылке описания документации
# в разделе Getting started: https://api.superjob.ru/#gettin.
# При регистрации приложения можно указать произвольные данные.

class ApiWork(ABC):
    def __init__(self):
        print("Connecting to API ...\n")

    @abstractmethod
    def get_vacancies(self):
        pass

    @staticmethod
    def select_platform():
        pass


class HeadHunterAPI(ApiWork):
    def get_vacancies(self, vacancy):
        """Парсинг вакансий"""
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": vacancy,
            "area": 1,  # Specify the desired area ID (1 is Moscow)
            "per_page": 10,  # Number of vacancies per page
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            vacancies = data.get("items", [])
            for vacancy in vacancies:
                # Extract relevant information from the vacancy object
                vacancy_id = vacancy.get("id")
                vacancy_title = vacancy.get("name")
                vacancy_url = vacancy.get("alternate_url")
                company_name = vacancy.get("employer", {}).get("name")
                print(f"ID: {vacancy_id}\nTitle: {vacancy_title}\nCompany:"
                      f" {company_name}\nURL: {vacancy_url}\n")
        else:
            print(f"Request failed with status code: {response.status_code}")


class SuperJobAPI():
    pass

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()

# Получение вакансий с разных платформ
hh_vacancies = hh_api.get_vacancies("")
# superjob_vacancies = superjob_api.get_vacancies("Python")


