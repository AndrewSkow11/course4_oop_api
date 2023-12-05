def predict_rub_salary(salary, currency_key, currency_code, from_key, to_key):
    if not salary[currency_key] == currency_code:
        return None
    if salary[from_key] and salary[to_key]:
        return (salary[from_key] + salary[to_key]) / 2
    if salary[from_key]:
        return salary[from_key] * 1.2
    if salary[to_key]:
        return salary[to_key] * 0.8