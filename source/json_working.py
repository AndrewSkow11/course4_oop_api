import json
from select import select

from source.vacancy import Vacancy


class JSONSaver:
    """Создание класса для работы с json файлом с вакансиями"""

    def __init__(self):
        print("Working with json ...")
        self.filename = 'VACANCY.json'

    def add_vacancies(self, vacancies_json):
        """Внесение данных о вакансиях в json файл"""

        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies_json, file, ensure_ascii=False, indent=4)

    def select(self):
        """Извлечение из json файла данных о вакансии с заданными параметрами"""
        with open(self.filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        vacancies = [Vacancy(x['id'],
                             x['title'],
                             x['url'],
                             x['salary_from'],
                             x['salary_to'],
                             x['employer'],
                             x['api']) for x in data]
        return vacancies

    # def sorted_vacancies_by_salary_from_asc(self):
    #     """Сортировка вакансий по минимальным зарплатам по возрастающей"""
    #     vacancies = self.select()
    #     vacancies = sorted(vacancies, key=lambda p: p.salary_from or 0)
    #     return vacancies

    def sorted_vacancies_by_salary_from_desc(self):
        """Сортировка вакансий по минимальным зарплатам по убывающей"""
        vacancies = self.select()
        vacancies = sorted(vacancies, reverse=True, key=lambda p: p.salary_from or 0)
        return vacancies

    # def sorted_vacancies_by_salary_to_asc(self):
    #     """Сортировка по максимальным заррплатам"""
    #     vacancies = self.select()
    #     vacancies = sorted(vacancies, key=lambda x: x.salary_to if x.salary_to else 0)
    #     return vacancies

    def get_vacancies_by_salary(self, num1, num2):
        vacancies = self.select()
        vacancies_by_salary = []

        for vac in vacancies:
            if vac.salary_from == num1 and vac.salary_to == num2:
                vacancies_by_salary.append(vac)

        return vacancies_by_salary

    def clear_vacancies(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write("")

    def filter_vacancies(self, list_of_word):
        vacancies = self.select()
        vacancies_filter = []

        for word in list_of_word:
            for vacancy in vacancies:
                if word in vacancy.title:
                    vacancies_filter.append(vacancy)

        return vacancies_filter

    # def sort_vacancies(self, vacancies):
    #
    #
    # def get_top_vacancies(self, sorted_vacancies, top_n):
    #     pass
    #
    # def print_vacancies(self, vacancies):
    #     pass
    #


