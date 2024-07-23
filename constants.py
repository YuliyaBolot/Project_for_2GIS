from string import punctuation


class Urls:
    url_receive_token = 'https://regions-test.2gis.com/v1/auth/tokens'
    url_create_place = 'https://regions-test.2gis.com/v1/favorites'


class Place:
    place_with_all_params = {
        "title": "Park",
        "lat": 55.023456,
        "lon": 82.048956,
        "color": "BLUE"
    }

    place_with_different_colors = [{
        "title": "Park",
        "lat": 55.023456,
        "lon": 82.048956,
        "color": "BLUE"
    },
        {
            "title": "Park",
            "lat": 55.023456,
            "lon": 82.048956,
            "color": "GREEN"
        },
        {
            "title": "Park",
            "lat": 55.023456,
            "lon": 82.048956,
            "color": "RED"
        },
        {
            "title": "Park",
            "lat": 55.023456,
            "lon": 82.048956,
            "color": "YELLOW"
        }
    ]

    place_without_color = {
        "title": "Park",
        "lat": 55.023456,
        "lon": 82.048956
    }

    place_with_incorrect_color = [{
        "title": "Park",
        "lat": 55.023456,
        "lon": 82.048956,
        "color": "BROWN"
    },
        {
            "title": "Park",
            "lat": 55.023456,
            "lon": 82.048956,
            "color": 1223456
        },
        {
            "title": "Park",
            "lat": 55.023456,
            "lon": 82.048956,
            "color": ""
        },
        {
            "title": "Park",
            "lat": 55.023456,
            "lon": 82.048956,
            "color": "BLACK"
        }
    ]

    place_with_different_titles = [{
        "title": "Central Park",
        "lat": 68.864567,
        "lon": 95.234567
    },
        {
            "title": "Центральный Парк",
            "lat": 68.864567,
            "lon": 95.234567
        },
        {
            "title": "Центральный Park",
            "lat": 68.864567,
            "lon": 95.234567
        },
        {
            "title": 1234455,
            "lat": 68.864567,
            "lon": 95.234567
        },
        {
            "title": punctuation,
            "lat": 68.864567,
            "lon": 95.234567
        },
        {
            "title": "W",
            "lat": 68.864567,
            "lon": 95.234567
        },
        {
            "title": "ЦБ",
            "lat": 68.864567,
            "lon": 95.234567
        },
        {
            "title": "ф" * 999,
            "lat": 68.864567,
            "lon": 95.234567
        },
        {
            "title": "y" * 998,
            "lat": 68.864567,
            "lon": 95.234567
        }
    ]

    place_without_title = {
        "lat": 68.864567,
        "lon": 95.234567
    }

    place_with_title1000 = {
        "title": "W" * 1000,
        "lat": 68.864567,
        "lon": 95.234567
    }

    place_with_null_title = {
        "title": "",
        "lat": 68.864567,
        "lon": 95.234567
    }

    place_without_lat = {
        "title": "Central Park",
        "lon": 95.234567
    }

    place_without_lon = {
        "title": "Центральный Парк",
        "lat": 68.864567
    }

    place_lat_with_letters = {
        "title": "Central Park",
        "lat": 'sskdlf;d;;fnfkdk',
        "lon": 95.234567
    }

    place_lon_with_letters = {
        "title": "Центральный Park",
        "lat": 68.864567,
        "lon": 'kddls;la;;a7'
    }

    place_with_lat_less_equals_90 = [{
        "title": "Центральный Park",
        "lat": 89.999999,
        "lon": 95.234567
    },
        {
            "title": "Центральный Park",
            "lat": 90.0,
            "lon": 95.234567
        }
    ]

    place_with_lat_more_than_90 = [{
        "title": "Центральный Park",
        "lat": 90.00000000000001,
        "lon": 95.234567
    },
        {
            "title": "Центральный Park",
            "lat": 90.000000000000001,
            "lon": 95.234567
        }
    ]

    place_with_lon_less_equals_180 = [{
        "title": "Центральный Park",
        "lat": 68.864567,
        "lon": 179.999999
    },
        {
            "title": "Центральный Park",
            "lat": 68.864567,
            "lon": 180.0
        }
    ]

    place_with_lon_more_than_180 = [{
        "title": "Центральный Park",
        "lat": 68.864567,
        "lon": 180.0000000000001
    },
        {
            "title": "Центральный Park",
            "lat": 68.864567,
            "lon": 180.00000000000001
        }
    ]

    place_with_string_lat_lon = {
        "title": "Центральный Park",
        "lat": '68.864567',
        "lon": '95.234567'
    }


class Message:
    message_wrong_color = "Параметр 'color' может быть одним из следующих значений: BLUE, GREEN, RED, YELLOW"
    message_required_lat = "Параметр 'lat' является обязательным"
    message_lat_is_number = "Параметр 'lat' должен быть числом"
    message_lat_less_equals_90 = "Параметр 'lat' должен быть не более 90"
    message_required_lon = "Параметр 'lon' является обязательным"
    message_lon_is_number = "Параметр 'lon' должен быть числом"
    message_lon_less_equals_180 = "Параметр 'lon' должен быть не более 180"
    message_token_is_required = "Параметр 'token' является обязательным"
    message_wrong_invalid_token = "Передан несуществующий или «протухший» 'token'"
    message_title_is_required = "Параметр 'title' является обзательным"
    message_title_not_more_999 = "Параметр 'title' должен содержать не более 999 символов"
    message_title_is_not_null = "Параметр 'title' не может быть пустым"
