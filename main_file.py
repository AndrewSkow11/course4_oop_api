from source.api_working import HeadHunterAPI, SuperJobAPI
from source.vacancy import Vacancy
from source.json_working import JSONSaver
import json

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()

# # Получение вакансий с разных платформ
hh_vacancies = hh_api.get_vacancies("Python")
# superjob_vacancies = superjob_api.get_vacancies("Python")

# only for tests
# vacancy = Vacancy("1234",
#                   "Разработчик C++",
#                   "https://somthhing.ru/vacancy1234",
#                   100_000,
#                   150_000,
#                   "Компания",
#                   "hh.ru")
# print(vacancy)


# Сохранение информации о вакансиях в файл
json_saver = JSONSaver()
json_saver.add_vacancies(hh_vacancies)
json_saver.get_vacancies_by_salary(8000, 25000)
# очистка списка
# json_saver.clear_vacancies()


# def filter_vacancies(js_object: JSONSaver, filter_words: list):
#     pass
#
#
def sort_vacancies(vacancies):
    vacancies = sorted(vacancies, reverse=True, key=lambda p: p.salary_from or 0)

    # for v in vacancies:
    #     print(v)

    return vacancies



def get_top_vacancies(vacancies, top_n):

    list_of_top_vacancies = []

    for number in range(top_n):
        list_of_top_vacancies.append(vacancies[number])

    for vacancy in list_of_top_vacancies:
        print("_____________")
        print(vacancy)

#
# def print_vacancies(vacancies):
#     pass
#


# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = ["HeadHunter", "SuperJob"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    hh_object = hh_api.get_vacancies(search_query)
    sj_object = superjob_api.get_vacancies(search_query)

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = json_saver.filter_vacancies(filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    # print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
