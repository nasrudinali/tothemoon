import requests

from package.core.headers import headers
from package.base import base
from package.core.info import asset


def get_planet(token, proxies=None):
    url = "https://moon.popp.club/moon/planets"

    try:
        response = requests.get(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        data = response.json()["data"]
        return data
    except:
        return None


def explore_planet(token, planet_id, proxies=None):
    url = f"https://moon.popp.club/moon/explorer?plantId={planet_id}"

    try:
        response = requests.get(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        data = response.json()
        return data
    except:
        return None


def process_explore_planet(token, proxies=None):
    planets = get_planet(token=token, proxies=proxies)
    if planets:
        for planet in planets:
            planet_id = planet["id"]
            start_explore_planet = explore_planet(
                token=token, planet_id=planet_id, proxies=proxies
            )
            explore_status = start_explore_planet["msg"]
            if explore_status == "success":
                explore_amount = start_explore_planet["data"]["amount"]
                explore_award = start_explore_planet["data"]["award"]
                base.log(
                    f"{base.white}Explore Planet: {base.green}Success {explore_amount} {explore_award}"
                )

                sd, probe, eth, invite_sd, farm_end_time, current_time = asset(
                    token=token, proxies=proxies
                )
                base.log(
                    f"{base.green}SD: {base.white}{sd} - {base.green}Probe: {base.white}{probe} - {base.green}ETH: {base.white}{eth}"
                )
            else:
                base.log(f"{base.white}Explore Planet: {base.red}Fail")
    else:
        base.log(f"{base.white}Explore Planet: {base.red}No planet to explore")
