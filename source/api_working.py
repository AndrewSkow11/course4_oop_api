class Engine(ABC):
    """Абстрактный класс"""
    @abstractmethod
    def get_request(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class HeadHunter(Engine):
    def __init__(self, keyword):
        self.keyword = keyword
        self.__header = {
            "User-Agent": "Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"}
        self.__params = {
            "text": keyword,
            "page": 0,
            "per_page": 100,
        }
        self.__vacancies = [] #список вакансий, который заполняется  по мерере получения данных по api

    @staticmethod
    def get_salary(salary):
        formatted_salary = [None, None]
        if salary and salary['from'] and salary['from'] != 0:
            formatted_salary[0] = salary['from'] if salary['currency'].lower() == 'rur' else salary['from'] * 76
        if salary and salary['to'] and salary['to'] != 0:
            formatted_salary[1] = salary['to'] if salary['currency'].lower() == 'rur' else salary['to'] * 76
        return formatted_salary

    """
    Получение значений через API
    """
    def get_request(self):
        response = requests.get("https://api.hh.ru/vacancies",
                                headers=self.__header,
                                params=self.__params)
        if response.status_code != 200:
            raise ParsingError
        return response.json()['items']

    def get_formatted_vacancies(self):
        formatted_vacancies = []
        for vacancy in self.__vacancies:
            salary_from, salary_to = self.get_salary(vacancy['salary'])
            formatted_vacancies.append({
                "id": vacancy["id"],
                "title": vacancy["name"],
                "url": vacancy["alternate_url"],
                "salary_from": salary_from,
                "salary_to": salary_to,
                "employer": vacancy['employer']["name"],
                "api": "HeadHunter",
            })
        return formatted_vacancies

    def get_vacancies(self, pages_count=1):
        while self.__params['page'] < pages_count:
            print(f"HeadHunter, Парсинг страницы {self.__params['page']+1}", end=": ")
            try:
                values = self.get_request()
            except ParsingError:
                print("Ошибка при получении данных")
                break
            print(f"Найдено ({len(values)}) вакансий.")
            self.__vacancies.extend(values)
            self.__params['page'] += 1


class SuperJob(Engine, ABC):
    def __init__(self, keyword):
        self.keyword = keyword
        self.__header = {"X-Api-App-Id": os.getenv("API_KEY_SJ")}
        self.__params = {
            "keyword": keyword,
            "page": 0,
            "count": 100,
        }
        self.__vacancies = []

    @staticmethod
    def get_salary(salary, currency):
        formatted_salary = None
        if salary and salary != 0:
            formatted_salary = salary if currency == 'rub' else salary['from'] * 76
        return formatted_salary

    def get_request(self):
        response = requests.get("https://api.superjob.ru/2.0/vacancies/",
                                headers=self.__header,
                                params=self.__params)
        print(response)
        if response.status_code != 200:
            raise ParsingError
        return response.json()['objects']

    def get_formatted_vacancies(self):
        formatted_vacancies = []
        for vacancy in self.__vacancies:
            formatted_vacancies.append({
                "id": vacancy["id"],
                "title": vacancy["profession"],
                "url": vacancy["link"],
                "salary_from": self.get_salary(vacancy['payment_from'], vacancy['currency']),
                "salary_to": self.get_salary(vacancy['payment_to'], vacancy['currency']),
                "employer": vacancy['firm_name'],
                "api": "SuperJob",
            })
        return formatted_vacancies

    def get_vacancies(self, pages_count=1):
        while self.__params['page'] < pages_count:
            print(f"SuperJob, Парсинг страницы {self.__params['page']+1}", end=": ")
            try:
                values = self.get_request()
            except ParsingError:
                print("Ошибка при получении данных")
                break
            print(f"Найдено ({len(values)}) вакансий.")
            self.__vacancies.extend(values)
            self.__params['page'] += 1