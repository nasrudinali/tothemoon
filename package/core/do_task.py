import requests

from package.core.headers import headers
from package.base import base


def visit_ss(token, proxies=None):
    url = "https://moon.popp.club/moon/task/visit/ss"

    try:
        response = requests.post(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        return response.json()
    except:
        return None


def task_list(token, proxies=None):
    url = "https://moon.popp.club/moon/task/list"

    try:
        response = requests.get(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        return response.json()
    except:
        return None


def check_task(token, task_id, proxies=None):
    url = f"https://moon.popp.club/moon/task/check?taskId={task_id}"

    try:
        response = requests.get(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        return response.json()
    except:
        return None


def claim_task(token, task_id, proxies=None):
    url = f"https://moon.popp.club/moon/task/claim?taskId={task_id}"

    try:
        response = requests.get(
            url=url, headers=headers(token), proxies=proxies, timeout=20
        )
        return response.json()
    except:
        return None


def process_do_task(token, proxies=None):
    process_visit_ss = visit_ss(token=token, proxies=proxies)
    get_task_list = task_list(token=token, proxies=proxies)
    if get_task_list:
        tasks = get_task_list["data"]
        for task in tasks:
            task_id = task["taskId"]
            task_name = task["name"]
            process_check_task = check_task(
                token=token, task_id=task_id, proxies=proxies
            )
            if process_check_task:
                task_progress = process_check_task["data"]
                if task_progress == 2:
                    base.log(f"{base.white}{task_name}: {base.green}Completed")
                else:
                    process_claim_task = claim_task(
                        token=token, task_id=task_id, proxies=proxies
                    )
                    if process_claim_task:
                        claim_task_status = process_claim_task["code"]
                        if claim_task_status == "400":
                            base.log(f"{base.white}{task_name}: {base.red}Incomplete")
                        elif claim_task_status == "00":
                            base.log(
                                f"{base.white}{task_name}: {base.green}Claim success"
                            )
                    else:
                        base.log(f"{base.red}Claim task error!s")
            else:
                base.log(f"{base.red}Check task error!")
    else:
        base.log(f"{base.red}Task list not found!")
