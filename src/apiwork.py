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
        print("Connecting to API ...")

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunterAPI(ApiWork):
    pass

class SuperJobAPI():
    pass



