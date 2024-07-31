import requests
from package.game_modules.start_game import headers
from package.base import Base

base = Base()


def check_in(token, proxies=None):
    url = "https://moon.popp.club/moon/sign/in"

    try:
        response = requests.post(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        check_in = response.json()
        check_in_status = check_in["code"]
        if check_in_status == "400":
            base.log(f"{base.white}Check-in: {base.red}Checked in today")
        elif check_in_status == "00":
            base.log(f"{base.white}Check-in: {base.green}Success")
    except:
        base.log(f"{base.white}Check-in: {base.red}Error")
