from abc import abstractmethod, ABC
import json

# 3
# Определить абстрактный класс, который обязывает реализовать
# методы для добавления вакансий в файл, получения данных из файла по указанным
# критериям и удаления информации о вакансиях.
# Создать класс для сохранения информации о вакансиях в JSON-файл.
# Дополнительно (по желанию) можно реализовать классы для работы с другими
# форматами, например с CSV-, Excel- или TXT-файлом.

class WorkFiles(ABC):
    @abstractmethod
    def add_vacancy(self, something_variable):
        pass

    @abstractmethod
    def add_vacancies(self, something_variable):
        pass


class WorkJSON(WorkFiles):
    def add_vacancy(self, one_vacancy):
        with open("vacancies.json", 'a'):
            json.load(one_vacancy)

    @abstractmethod
    def add_vacancies(self, list_of_vacancy):
        with open("vacancies.json", 'a'):
            json.loads(list_of_vacancy)



