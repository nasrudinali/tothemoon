import requests

from package.core.headers import headers
from package.base import base
from package.core.info import asset


def claim_farm(token, proxies=None):
    url = "https://moon.popp.club/moon/claim/farming"

    try:
        response = requests.get(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        data = response.json()
        return data
    except:
        return None


def start_farm(token, proxies=None):
    url = f"https://moon.popp.club/moon/farming"

    try:
        response = requests.get(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        data = response.json()
        return data
    except:
        return None


def process_farming(token, proxies=None):
    process_claim_farm = claim_farm(token=token, proxies=proxies)
    claim_farm_status = process_claim_farm["msg"]
    if claim_farm_status == "success":
        base.log(f"{base.white}Claim Farming: {base.green}Success")
    else:
        base.log(f"{base.white}Claim Farming: {base.red}Fail")
    process_start_farm = start_farm(token=token, proxies=proxies)
    start_farm_status = process_start_farm["msg"]
    if start_farm_status == "success":
        base.log(f"{base.white}Start Farming: {base.green}Success")
    else:
        base.log(f"{base.white}Start Farming: {base.red}In farming status")

    sd, probe, eth, invite_sd, farm_end_time, current_time = asset(
        token=token, proxies=proxies
    )
    base.log(
        f"{base.green}SD: {base.white}{sd} - {base.green}Probe: {base.white}{probe} - {base.green}ETH: {base.white}{eth}"
    )
    time_left = (farm_end_time - current_time) / 1000
    return time_left
