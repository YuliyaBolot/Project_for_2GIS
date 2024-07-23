import requests
import allure
from constants import Urls


class Helpers:
    @allure.step('Получение сессионного токена')
    def get_token(self):
        response_post = requests.post(Urls.url_receive_token)
        token = response_post.cookies
        return f'token={token['token']}'
