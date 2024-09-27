import requests


def get_random_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    headers = {
        "x-api-key": "live_PyQbnUAYcaTH9szyXhRWO7wERj86DhVLR9nGMUmucJ7gbtzYmbQahKX8ffi8FdH5"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data[0]['url']  # Возвращаем URL изображения
    return None  # Возвращаем None в случае неуспешного запроса
