from src.apiwork import ApiWork
from src.vacancy import Vacancy

# 5
# Объединить все классы и функции в единую программу.

# Выходные данные
# Информация о вакансиях, полученная с разных платформ, сохраненная в JSON-файл.
# Отфильтрованные и отсортированные вакансии, выводимые пользователю через консоль.

# вызываем абстрактный метод для выбора платформы и дальнейшей работы
# создаём базовый список для дальнейшей обработки
# с учётом 3 параметров: сайт, ключевое слово, количество вакансий
base_list_of_vacancies = ApiWork.select_api()

for vacancy in base_list_of_vacancies:
    print(vacancy)

list_of_objects_vacancy = (Vacancy.
                           initialize_base_list_of_objects
                           (base_list_of_vacancies))

for i in list_of_objects_vacancy:
    print(i)

# Создание экземпляра класса для работы с вакансиями
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")

# # Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
# json_saver.delete_vacancy(vacancy)
#
# # Функция для взаимодействия с пользователем
# def user_interaction():
#     platforms = ["HeadHunter", "SuperJob"]
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#
#
#
#
#
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)
#
#     if not filtered_vacancies:
#         print("Нет вакансий, соответствующих заданным критериям.")
#         return
#
#     sorted_vacancies = sort_vacancies(filtered_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)


# if __name__ == "__main__":
#     user_interaction()