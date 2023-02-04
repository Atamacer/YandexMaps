import requests

server = 'http://static-maps.yandex.ru/1.x/'


def get_img(
        scale=[0.1, 0.1],
        coords=[51.297974, 37.833231]
):
    parametrs = {
        'll': str(coords[1]) + ',' + str(coords[0]),
        'spn': str(scale[1]) + ',' + str(scale[0]),
        'l': 'map'}
    response = requests.get(server, params=parametrs)

    return response
