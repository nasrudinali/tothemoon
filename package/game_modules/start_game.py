import requests
import json
import urllib.parse


def headers(token=None):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://planet.popp.club",
        "Referer": "https://planet.popp.club/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    if token:
        headers["Authorization"] = token
    return headers


def parse_query_id(data):
    parsed_query = urllib.parse.parse_qs(data)
    final_json = {}
    for key, values in parsed_query.items():
        if key == "user" and values:
            user_json_str = values[0]
            final_json[key] = json.loads(urllib.parse.unquote(user_json_str))
        else:
            final_json[key] = values[0] if values else None
    return final_json


def get_token(data, proxies=None):
    url = "https://moon.popp.club/pass/login"
    data = {
        "initData": f"{data}",
        "initDataUnSafe": parse_query_id(data=data),
    }

    try:
        response = requests.post(
            url=url, headers=headers(), json=data, proxies=proxies, timeout=20
        )
        token = response.json()["data"]["token"]
        return token
    except:
        return None
