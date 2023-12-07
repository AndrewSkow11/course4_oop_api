from abc import ABC, abstractmethod
from os import getenv
import requests


class ConnectAPI(ABC):
    pass


class HeadHunterAPI(ConnectAPI):
    def __init__(self):
        print("\033[33mConnecting to API ... hh.ru\033[0m")
        self.vacancies = []


    @staticmethod
    def get_salary(salary):
        """Метод возвращает зарплату списком ['от', 'до']"""
        formatted_salary = [None, None]

        if salary and salary['from'] and salary['from'] != 0:
            formatted_salary[0] = salary['from'] if salary['currency'].lower() == 'rur' else salary['from'] * 76
        if salary and salary['to'] and salary['to'] != 0:
            formatted_salary[1] = salary['to'] if salary['currency'].lower() == 'rur' else salary['to'] * 76
        return formatted_salary

    def get_vacancies(self, keyword):
        params = {
            "text": keyword,
            "page": 0,
            "per_page": 100,
        }
        response = requests.get("https://api.hh.ru/vacancies",
                                params=params)
        if response.status_code != 200:
            print("Не удалось совершить запрос")

        print("Тип данных", type(response.json()['items']))

        for vacancy in response.json()['items']:
            salary_from, salary_to = self.get_salary(vacancy['salary'])
            self.vacancies.append({
                "id": vacancy["id"],
                "title": vacancy["name"],
                "url": vacancy["alternate_url"],
                "salary_from": salary_from,
                "salary_to": salary_to,
                "employer": vacancy['employer']["name"],
                "api": "HeadHunter",
            })
        return self.vacancies

    # def get_formatted_vacancies(self):
    #     formatted_vacancies = []
    #     for vacancy in self.vacancies:
    #         salary_from, salary_to = self.get_salary(vacancy['salary'])
    #         formatted_vacancies.append({
    #             "id": vacancy["id"],
    #             "title": vacancy["name"],
    #             "url": vacancy["alternate_url"],
    #             "salary_from": salary_from,
    #             "salary_to": salary_to,
    #             "employer": vacancy['employer']["name"],
    #             "api": "HeadHunter",
    #         })
    #     return formatted_vacancies

    # def get_vacancies(self, pages_count=1):
    #     while self.params['page'] < pages_count:
    #         print(f"HeadHunter, Парсинг страницы {self.params['page'] + 1}", end=": ")
    #         try:
    #             values = self.get_request()
    #         except Exception:
    #             print("Ошибка при получении данных")
    #             break
    #         print(f"Найдено ({len(values)}) вакансий.")
    #         self.vacancies.extend(values)
    #         self.params['page'] += 1


class SuperJobAPI(ConnectAPI, ABC):
    def __init__(self):
        print("\033[33mConnecting to API ... superjob.ru\033[0m")
        self.header = {"X-Api-App-Id": getenv("API_KEY_SJ")}
        self.vacancies = []

    @staticmethod
    def get_salary(salary, currency):
        formatted_salary = None
        if salary and salary != 0:
            formatted_salary = salary if currency == 'rub' else salary['from'] * 76
        return formatted_salary

    def get_vacancies(self, keyword):
        params = {
            "keyword": keyword,
            "page": 0,
            "count": 100,
        }

        response = requests.get("https://api.superjob.ru/2.0/vacancies/",
                                headers=self.header,
                                params=params)
        if response.status_code != 200:
            print("Ошибка при обращении к сайту superjob.ru")
        # return response.json()['objects']

        for vacancy in response.json()['objects']:
            self.vacancies.append({
                "id": vacancy["id"],
                "title": vacancy["profession"],
                "url": vacancy["link"],
                "salary_from": self.get_salary(vacancy['payment_from'], vacancy['currency']),
                "salary_to": self.get_salary(vacancy['payment_to'], vacancy['currency']),
                "employer": vacancy['firm_name'],
                "api": "SuperJob",
            })
        return self.vacancies


    # def get_formatted_vacancies(self):
    #     formatted_vacancies = []
    #     for vacancy in self.vacancies:
    #         formatted_vacancies.append({
    #             "id": vacancy["id"],
    #             "title": vacancy["profession"],
    #             "url": vacancy["link"],
    #             "salary_from": self.get_salary(vacancy['payment_from'], vacancy['currency']),
    #             "salary_to": self.get_salary(vacancy['payment_to'], vacancy['currency']),
    #             "employer": vacancy['firm_name'],
    #             "api": "SuperJob",
    #         })
    #     return formatted_vacancies

    # def get_vacancies(self, pages_count=1):
    #     while self.params['page'] < pages_count:
    #         print(f"SuperJob, Парсинг страницы {self.params['page'] + 1}", end=": ")
    #         try:
    #             values = self.get_request()
    #         except Exception:
    #             print("Ошибка при получении данных c сайта superjob.ru")
    #             break
    #         print(f"Найдено ({len(values)}) вакансий.")
    #         self.vacancies.extend(values)
    #         self.params['page'] += 1
    #

# sj = SuperJobAPI("python")
# # sj.get_vacancies()
