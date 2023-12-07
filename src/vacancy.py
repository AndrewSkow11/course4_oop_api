from abc import abstractmethod

# 2
# Создать класс для работы с вакансиями.
# В этом классе самостоятельно определить атрибуты,
# такие как название вакансии, ссылка на вакансию,
# зарплата, краткое описание или требования и т. п. (не менее четырех).
# Класс должен поддерживать методы сравнения вакансий между собой по зарплате
# и валидировать данные, которыми инициализируются его атрибуты.


# vacancy = Vacancy("Python Developer",
# "<https://hh.ru/vacancy/123456>",
# "100 000-150 000 руб.",
# "Требования: опыт работы от 3 лет...")


class Vacancy:
    def __init__(self, title=None, url=None, salary_from=None,
                 salary_to=None, experience=None):
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.experience = experience

    def __str__(self):
        return (f'\nЗаголовок: {self.title}\n'
                f'Ссылка: {self.url}\n'
                f'Зарплата (от): {self.salary_from}\n'
                f'Зарплата (до): {self.salary_to}\n'
                f'Опыт: {self.experience}\n'
                )

    def make_dictionary(self):
        dict_vacancy = {
            'Заголовок': self.title,
            'Ссылка': self.url,
            'Зарплата (от)': self.salary_from,
            'Зарплата (до)': self.salary_to,
            'Опыт': self.experience
        }
        return dict_vacancy

    # написать магические методы сравнения по зарплате

    @classmethod
    def initialize_base_list_of_objects(cls, base_list_of_vacancies):
        list_of_objects_vacancy = []

        try:
            # если вакансия от superjob.ru
            (base_list_of_vacancies[0]['canEdit'])
            for vacancy in base_list_of_vacancies:
                list_of_objects_vacancy.append(Vacancy(
                    vacancy.get('profession', '-'),
                    vacancy.get('link', '-'),
                    vacancy.get('payment_from', '-'),
                    vacancy.get('payment_to', '-'),
                    vacancy.get('experience', '-').get('title', '-')))
            return list_of_objects_vacancy

        except KeyError:
            # значит вакансия от hh.ru
            for vacancy in base_list_of_vacancies:
                list_of_objects_vacancy.append(Vacancy(
                    vacancy.get('name'),
                    vacancy.get('alternate_url'),
                    vacancy.get('salary').get('from'),
                    vacancy.get('salary').get('to'),
                    vacancy.get('experience').get('name')))
            return list_of_objects_vacancy