from source.api_working import HeadHunterAPI, SuperJobAPI
from source.json_working import JSONSaver

def sort_vacancies(vacancies):
    vacancies = sorted(vacancies, reverse=True,
                       key=lambda p: p.salary_from or 0)
    return vacancies

def print_top_vacancies(vacancies, top_n):
    list_of_top_vacancies = []
    try:
        for number in range(top_n):
            list_of_top_vacancies.append(vacancies[number])
    except IndexError:
        print(f"Топ-ваканский меньше {top_n}")

    for vacancy in list_of_top_vacancies:
        print("\n_____________")
        print(vacancy)


# Функция для взаимодействия с пользователем
def user_interaction():
    user_input = int(input("Если вы хотите получить вакансии с сайта hh.ru"
                           " введите \033[36m0\n"
                           "\033[0mЕсли вы хотите получить вакансии с сайта"
                           "superjob.ru нажмите \033[36m1\n\033[0m>> "))

    platforms = ["HeadHunter", "SuperJob"]

    if user_input == 0:
        print(f"\nВы предпочли вакансии с сайта "
              f"\033[92m{platforms[0]}")
        hh_api = HeadHunterAPI()

        search_query = input("Введите поисковый запрос: ")
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        hh = hh_api.get_vacancies(search_query)

        json_saver = JSONSaver()
        json_saver.add_vacancies(hh)

        filter_words = input(
            "Введите ключевые слова для фильтрации вакансий: ").split()
        filtered_vacancies = json_saver.filter_vacancies(filter_words)

        if not filtered_vacancies:
            print("Нет вакансий, соответствующих заданным критериям.")
            return

        sorted_vacancies = sort_vacancies(filtered_vacancies)
        print_top_vacancies(sorted_vacancies, top_n)

        json_saver = JSONSaver()
        json_saver.add_vacancies(hh)

        print("______________\nПрограмма завершена\n")

    elif user_input == 1:
        print(f"\nВы предпочли вакансии с сайта "
              f"\033[92m{platforms[0]}")
        superjob_api = SuperJobAPI()

        search_query = input("Введите поисковый запрос: ")
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
        sj = superjob_api.get_vacancies(search_query)

        json_saver = JSONSaver()
        json_saver.add_vacancies(sj)

        filter_words = input(
            "Введите ключевые слова для фильтрации вакансий: ").split()
        filtered_vacancies = json_saver.filter_vacancies(filter_words)

        if not filtered_vacancies:
            print("Нет вакансий, соответствующих заданным критериям.")
            return

        sorted_vacancies = sort_vacancies(filtered_vacancies)
        print_top_vacancies(sorted_vacancies, top_n)

        json_saver = JSONSaver()
        json_saver.add_vacancies(sj)

        print("______________\nПрограмма завершена\n")

    else:
        print("Ошибочный ввод, программа завершена")


if __name__ == "__main__":
    user_interaction()
