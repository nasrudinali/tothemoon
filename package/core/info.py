import requests

from package.core.headers import headers


def asset(token, proxies=None):
    url = "https://moon.popp.club/moon/asset"

    try:
        response = requests.get(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        asset = response.json()
        sd = asset["data"]["sd"]
        probe = asset["data"]["probe"]
        eth = asset["data"]["eth"]
        invite_sd = asset["data"]["frozenInviteSd"]
        farm_end_time = asset["data"]["farmingEndTime"]
        current_time = asset["data"]["systemTimestamp"]
        return sd, probe, eth, invite_sd, farm_end_time, current_time
    except:
        return None
