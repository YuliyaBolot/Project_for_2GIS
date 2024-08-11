import requests
import pytest
import allure
from constants import Urls, Place, Message
from helpers import Helpers


class TestCreateFavouritePlaceColors:
    @allure.title('Создание избранного места с цветами иконок: BLUE, GREEN, RED, YELLOW')
    @pytest.mark.parametrize('place_with_different_colors', Place.place_with_different_colors)
    def test_create_favourite_place_with_different_colors(self, place_with_different_colors):
        helper = Helpers()
        token = helper.get_token()
        place = place_with_different_colors
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        color = response.json()['color']
        assert 200 == response.status_code and color == place['color']

    @allure.title('Создание избранного места без указания цвета иконки')
    def test_create_favourite_place_without_color(self):
        helper = Helpers()
        token = helper.get_token()
        place = Place.place_without_color
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        color = response.json()['color']
        assert 200 == response.status_code and color is None

    @allure.title('Попытка создать избранное место с цветами иконок, отличными от BLUE, GREEN, RED, YELLOW')
    @allure.issue('BUG: Проходит тест с цветом BROWN')
    @pytest.mark.parametrize('incorrect_color', Place.place_with_incorrect_color)
    def test_create_favourite_place_with_incorrect_colors(self, incorrect_color):
        helper = Helpers()
        token = helper.get_token()
        place = incorrect_color
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        message = Message.message_wrong_color
        assert 400 == response.status_code and response.json()['error']['message'] == message
