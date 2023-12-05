import requests, os, pprint
from itertools import islice, count
from common import predict_rub_salary


def request_super_job(params={}):

    headers = {
        'Host': 'api.superjob.ru',
        'X-Api-App-Id': os.getenv('API_KEY'),
        'Authorization': 'Bearer r.000000010000001.example.access_token',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params).json()
    return data


def fetch_all_pages(default_params={}):
    response = request_super_job(default_params)
    for page in count(0):
        params = {**default_params, 'count': 100}
        total_pages = round(response['total'] / params['count'])
        page_data = response
        if page > total_pages:
            break
        yield from page_data['objects']


def get_average_salary(params={}):
    vacancies = fetch_all_pages(params)
    args = ['currency', 'rub', 'payment_from', 'payment_to']
    predicted_salary_list = [predict_rub_salary(vacancy, *args) for vacancy in vacancies
                   if predict_rub_salary(vacancy, *args)]
    if not predicted_salary_list:
        return None
    return {'average_salary': round(sum(predicted_salary_list) / len(predicted_salary_list), 2),
            'vacancies_processed': len(predicted_salary_list)}



print(request_super_job())
print(get_average_salary())

