import requests
import allure
from constants import Urls, Place
from helpers import Helpers


class TestCreatePlace:
    @allure.title('Создание избранного места с корректными параметрами')
    def test_create_place(self):
        helper = Helpers()
        token = helper.get_token()
        place = Place.place_with_all_params
        response = requests.post(Urls.url_create_place, headers={'Cookie': token}, data=place)
        title = response.json()['title']
        lat = response.json()['lat']
        lon = response.json()['lon']
        color = response.json()['color']
        assert 200 == response.status_code and title == place['title'] and lat == place['lat'] and lon == place[
            'lon'] and color == place['color']
