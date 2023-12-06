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
    def __init__(self, title, url, salary, experience):
        self.title = title
        self.url = url
        self.salary = salary
        self.experience = experience

    def __str__(self):
        return (f'\nЗаголовок: {self.title}\n'
                f'Ссылка: {self.url}\n'
                f'Зарплата (от): {self.salary}\n'
                f'Опыт: {self.experience}\n'
                )

    # написать магические методы сравнения по зарплате


    @abstractmethod
    def initialize_base_list_of_objects(base_list_of_vacancies):
        list_of_objects_vacancy = []

        try:
            # если вакансия от superjob.ru
            (base_list_of_vacancies[0]['canEdit'])
            for vacancy in base_list_of_vacancies:
                list_of_objects_vacancy.append(Vacancy(
                    vacancy['profession'],
                    vacancy['link'],
                    vacancy['payment_from'],
                    vacancy['experience']['title']))
            return list_of_objects_vacancy

        except KeyError:
            # значит вакансия от hh.ru
            for vacancy in base_list_of_vacancies:
                list_of_objects_vacancy.append(Vacancy(
                    vacancy['name'],
                    vacancy['alternate_url'],
                    vacancy['salary']['from'],
                    vacancy['experience']['name']))
            return list_of_objects_vacancy


