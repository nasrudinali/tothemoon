import requests

from package.core.headers import headers
from package.base import base


def process_claim_invite(token, proxies=None):
    url = "https://moon.popp.club/moon/claim/invite"

    try:
        response = requests.get(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        data = response.json()
        status = data["msg"]
        if status == "success":
            base.log(f"{base.white}Claim Invite: {base.green}Success")
        else:
            base.log(f"{base.white}Claim Invite: {base.red}Fail")
    except:
        base.log(f"{base.white}Claim Invite: {base.red}Error")
