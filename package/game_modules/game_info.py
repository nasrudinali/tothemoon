import requests
from package.game_modules.start_game import headers


def asset(token, proxies=None):
    url = "https://moon.popp.club/moon/asset"

    try:
        response = requests.get(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        game_info = response.json()
        return game_info
    except:
        return None
