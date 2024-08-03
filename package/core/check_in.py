import requests

from package.core.headers import headers
from package.base import base


def process_check_in(token, proxies=None):
    url = "https://moon.popp.club/moon/sign/in"

    try:
        response = requests.post(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        data = response.json()
        status = data["code"]
        if status == "400":
            base.log(f"{base.white}Check-in: {base.red}Checked in today")
        elif status == "00":
            base.log(f"{base.white}Check-in: {base.green}Success")
    except:
        base.log(f"{base.white}Check-in: {base.red}Error")
