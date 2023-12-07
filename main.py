from src.apiwork import ApiWork
from src.vacancy import Vacancy
from src.add_to_file import WorkJSON
import json

# 5
# Объединить все классы и функции в единую программу.

# Выходные данные
# Информация о вакансиях, полученная с разных платформ, сохраненная в JSON-файл.
# Отфильтрованные и отсортированные вакансии, выводимые пользователю через консоль.

# вызываем абстрактный метод для выбора платформы и дальнейшей работы
# создаём базовый список для дальнейшей обработки
# с учётом 3 параметров: сайт, ключевое слово, количество вакансий

base_list_of_vacancies = ApiWork.select_api()

list_of_objects_vacancy = (Vacancy.
                           initialize_base_list_of_objects
                           (base_list_of_vacancies))

# показываем для пользователя в отформатированном виде вакансии
for vacancy in list_of_objects_vacancy:
    print(vacancy)





# Сохранение информации о вакансиях в файл
for vacancy in list_of_objects_vacancy:
    vacancy_json = json.dumps(vacancy.make_dictionary(), ensure_ascii=False)
    with open('new_file.json', 'a', encoding='utf-8') as file:
        file.write(vacancy_json)

# json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
# json_saver.delete_vacancy(vacancy)


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
