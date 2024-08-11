import requests
import allure
import time
from constants import Urls, Place, Message
from helpers import Helpers


class TestTryToCreatePlaceWithoutToken:
    @allure.title('Попытка создать избранное место без токена')
    def test_create_place_without_token(self):
        place = Place.place_with_all_params
        response = requests.post(Urls.url_create_place, data=place)
        message = Message.message_token_is_required
        assert 401 == response.status_code and response.json()['error']['message'] == message

    @allure.title('Попытка создать избранное место с указанием некорректного токена')
    def test_create_place_with_wrong_token(self):
        token = f'token=faf9abb9396247abb4'
        place = Place.place_with_all_params
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        message = Message.message_wrong_invalid_token
        assert 401 == response.status_code and response.json()['error']['message'] == message

    @allure.title('Попытка создать избранное место с устаревшим токеном (более 2 секунд)')
    def test_create_place_with_invalid_token(self):
        helper = Helpers()
        token = helper.get_token()
        place = Place.place_with_all_params
        time.sleep(3)
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        message = Message.message_wrong_invalid_token
        assert 401 == response.status_code and response.json()['error']['message'] == message
