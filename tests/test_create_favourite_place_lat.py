import requests
import pytest
import allure
from constants import Urls, Place, Message
from helpers import Helpers


class TestCreateFavouritePlaceLat:
    @allure.title('Попытка создания избранного места без указания широты')
    def test_create_favourite_place_without_lat(self):
        helper = Helpers()
        token = helper.get_token()
        place = Place.place_without_lat
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        message = Message.message_required_lat
        assert 400 == response.status_code and response.json()['error']['message'] == message

    @allure.title('Попытка создания избранного места с указанием широты буквами')
    def test_create_favourite_place_letter_lat(self):
        helper = Helpers()
        token = helper.get_token()
        place = Place.place_lat_with_letters
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        message = Message.message_lat_is_number
        assert 400 == response.status_code and response.json()['error']['message'] == message

    @allure.title('Создание избранного места с широтой <= |90|')
    @pytest.mark.parametrize('lat_less_equals_abs90', Place.place_with_lat_less_equals_abs90)
    def test_create_favourite_place_with_lat_less_equals_90(self, lat_less_equals_abs90):
        helper = Helpers()
        token = helper.get_token()
        place = lat_less_equals_abs90
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        lat = response.json()['lat']
        assert 200 == response.status_code and lat == place['lat']

    @allure.title('Попытка создания избранного места с широтой > 90')
    @allure.issue('BUG: При указании 1 на 15-ом месте после запятой, происходит округление до 90.0')
    @pytest.mark.parametrize('lat_more_than_90', Place.place_with_lat_more_than_90)
    def test_create_favourite_place_with_lat_more_than_90(self, lat_more_than_90):
        helper = Helpers()
        token = helper.get_token()
        place = lat_more_than_90
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        message = Message.message_lat_less_equals_90
        assert 400 == response.status_code and response.json()['error']['message'] == message

    @allure.title('Попытка создания избранного места с широтой > -90')
    @allure.issue('BUG: При указании 1 на 15-ом месте после запятой, происходит округление до -90.0')
    @pytest.mark.parametrize('lat_more_than_minus_90', Place.place_with_lat_more_than_minus_90)
    def test_create_favourite_place_with_lat_more_than_minus_90(self, lat_more_than_minus_90):
        helper = Helpers()
        token = helper.get_token()
        place = lat_more_than_minus_90
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        message = Message.message_lat_less_equals_minus_90
        assert 400 == response.status_code and response.json()['error']['message'] == message

    @allure.title('Создание избранного места с нулевой широтой')
    def test_create_favourite_place_with_zero_lat(self):
        helper = Helpers()
        token = helper.get_token()
        place = Place.place_with_zero_lat
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        lat = response.json()['lat']
        assert 200 == response.status_code and lat == 0.0

    @allure.title('Создание избранного места с нулевой широтой и долготой')
    @allure.issue('BUG: Тест не проходит, возникает ошибка - файл не соответствует формату JSON.')
    def test_create_favourite_place_with_zero_lat_lon(self):
        helper = Helpers()
        token = helper.get_token()
        place = Place.place_with_zero_lat_lon
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        lat = response.json()['lat']
        lon = response.json()['lon']
        assert 200 == response.status_code and lat == 0.0 and lon == 0.0

    @allure.title('Проверка преобразования значения широты из строки в вещественное число')
    def test_create_favourite_place_with_string_lat(self):
        helper = Helpers()
        token = helper.get_token()
        place = Place.place_with_string_lat
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        lat = response.json()['lat']
        assert 200 == response.status_code and lat == float(place['lat'])
