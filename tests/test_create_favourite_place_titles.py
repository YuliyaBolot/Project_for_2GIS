import requests
import pytest
import allure
from constants import Urls, Place, Message
from helpers import Helpers


class TestCreateFavouritePlaceTitles:
    @allure.title('''Создание избранного места с различными загаловками: 
        лат. и кирилл. символы, цифры, знаки препинания, граничные и приграничные значения''')
    @pytest.mark.parametrize('place_with_different_titles', Place.place_with_different_titles)
    def test_create_favourite_place_with_different_titles(self, place_with_different_titles):
        helper = Helpers()
        token = helper.get_token()
        place = place_with_different_titles
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        title = response.json()['title']
        assert 200 == response.status_code and title == str(place['title'])

    @allure.title('Попытка создать избранное место без загаловка')
    def test_create_favourite_place_without_title(self):
        helper = Helpers()
        token = helper.get_token()
        place = Place.place_without_title
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        message = Message.message_title_is_required
        assert 400 == response.status_code and response.json()['error']['message'] == message

    @allure.title('Попытка создать избранное место с 1000 символов в загаловке')
    @allure.issue('BUG: Заголовок создается с 1000 символов')
    def test_create_favourite_place_with_1000title(self):
        helper = Helpers()
        token = helper.get_token()
        place = Place.place_with_title1000
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        message = Message.message_title_not_more_999
        assert 400 == response.status_code and response.json()['error']['message'] == message

    @allure.title('Попытка создать избранное место с пустым загаловком')
    def test_create_favourite_place_with_null_title(self):
        helper = Helpers()
        token = helper.get_token()
        place = Place.place_with_null_title
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        message = Message.message_title_is_not_null
        assert 400 == response.status_code and response.json()['error']['message'] == message
