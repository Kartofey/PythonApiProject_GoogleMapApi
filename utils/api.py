from utils.http_methods import Http_methods

base_url = "https://rahulshettyacademy.com"  #Базовый url
key = "?key=qaclick123"  #Параметр для всех запросов

# Методы для тестирования Google map api
class Google_map_api(): 

# Метод для создания новой локации
    @staticmethod
    def create_new_place():

        json_for_create_new_location = {
            "location": { 
            "lat": -38.383494, 
            "lng": 33.427362 
            }, "accuracy": 50, 
            "name": "Frontline house", 
            "phone_number": "(+91) 983 893 3937", 
            "address": "29, side layout, cohen 09", 
            "types": [
            "shoe park", 
            "shop"
            ],
            "website": "http://google.com", 
            "language": "French-IN"
        }

        post_resourse = "/maps/api/place/add/json"  #Ресурс метода Post
        post_url = base_url + post_resourse + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_location)
        print(result_post.text)
        return result_post


# Метод для проверки создания новой локации
    @staticmethod
    def get_new_place(place_id):
        get_resourse = "/maps/api/place/get/json"           #Ресурс метода Get
        get_url = base_url + get_resourse + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

# Метод для изменения адреса созданой локации
    @staticmethod
    def put_new_place(place_id):
        
        put_resourse = "/maps/api/place/update/json"            #Ресурс метода Put
        put_url = base_url + put_resourse + key
        print(put_url)
        
        json_for_update_new_location = {
            "place_id":place_id,
            "address":"110 Lenina street, RU",
            "key":"qaclick123"
        }

        result_put = Http_methods.put(put_url, json_for_update_new_location)
        print(result_put.text)
        return result_put

# Метод для удаления созданой локации
    def delete_new_place(place_id):
        delete_resourse = "/maps/api/place/delete/json"         #Ресурс метода Delete
        delete_url = base_url + delete_resourse + key
        print(delete_url)
        
        json_for_delete_new_location = {
            "place_id":place_id
        }
        result_delete = Http_methods.delete(delete_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete