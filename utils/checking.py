from requests import Response
import json

# Методы для проверки ответов наших запросов
class Checking():

# Метод для проверки статус кода
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Успешно. Статус код: " + str(response.status_code))
        else:
            print("Провал. Статус код: " + str(response.status_code))

# Метод для проверки обязательных полей в ответе запроса
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствут")

# Метод для проверки значений обязательных полей в ответе запроса
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верен.")

# Метод для проверки ожидаемых слов в обязательных полях в ответе запроса
    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Слово" + search_word + " присутсвует.")
        else:
            print("Слово" + search_word + " отсутсвует.")
