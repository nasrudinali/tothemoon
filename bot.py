import sys

sys.dont_write_bytecode = True

from package import Base
from package.game_modules import (
    start_game,
    game_info,
    process_check_in,
    process_do_task,
)
import time

base = Base()


class ToTheMoon:
    def __init__(self):
        # Get file directory
        self.data_file = base.file_path(file_name="data.txt")
        self.config_file = base.file_path(file_name="config.json")

        # Initialize line
        self.line = base.create_line(length=50)

        # Initialize banner
        self.banner = base.create_banner(game_name="To The Moon")

        # Get config
        self.auto_check_in = base.get_config(
            config_file=self.config_file, config_name="auto-check-in"
        )

        self.auto_do_task = base.get_config(
            config_file=self.config_file, config_name="auto-do-task"
        )

        self.auto_claim_invite = base.get_config(
            config_file=self.config_file, config_name="auto-claim-invite"
        )

        self.auto_explore_planet = base.get_config(
            config_file=self.config_file, config_name="auto-explore-planet"
        )

        self.auto_farm = base.get_config(
            config_file=self.config_file, config_name="auto-farm"
        )

    def main(self):
        while True:
            base.clear_terminal()
            print(self.banner)
            data = open(self.data_file, "r").read().splitlines()
            num_acc = len(data)
            base.log(self.line)
            base.log(f"{base.green}Numer of accounts: {base.white}{num_acc}")
            time_left_list = []

            for no, data in enumerate(data):
                base.log(self.line)
                base.log(f"{base.green}Account number: {base.white}{no+1}/{num_acc}")

                # Get token
                token = start_game.get_token(data=data)

                if token:
                    # Get game info
                    asset = game_info.asset(token=token)
                    sd = asset["data"]["sd"]
                    probe = asset["data"]["probe"]
                    eth = asset["data"]["eth"]
                    invite_sd = asset["data"]["frozenInviteSd"]
                    farm_end_time = asset["data"]["farmingEndTime"]
                    current_time = asset["data"]["systemTimestamp"]
                    base.log(
                        f"{base.green}SD: {base.white}{sd} - {base.green}Probe: {base.white}{probe} - {base.green}ETH: {base.white}{eth}"
                    )

                    # Check in
                    if self.auto_check_in:
                        base.log(f"{base.yellow}Auto Check-in: {base.green}ON")
                        process_check_in.check_in(token=token)
                    else:
                        base.log(f"{base.yellow}Auto Check-in: {base.red}OFF")

                    # Do task
                    if self.auto_do_task:
                        base.log(f"{base.yellow}Auto Do Task: {base.green}ON")
                        process_do_task.do_task(token=token)
                    else:
                        base.log(f"{base.yellow}Auto Do Task: {base.red}OFF")

                else:
                    base.log(f"{base.red}Token not found! Please get new query id")

            print()
            if time_left_list:
                wait_time = min(time_left_list) + 10
            else:
                wait_time = 10 * 60

            wait_hours = int(wait_time // 3600)
            wait_minutes = int((wait_time % 3600) // 60)
            wait_seconds = int(wait_time % 60)

            wait_message_parts = []
            if wait_hours > 0:
                wait_message_parts.append(f"{wait_hours} hours")
            if wait_minutes > 0:
                wait_message_parts.append(f"{wait_minutes} minutes")
            if wait_seconds > 0:
                wait_message_parts.append(f"{wait_seconds} seconds")

            wait_message = ", ".join(wait_message_parts)
            base.log(f"{base.yellow}Wait for {wait_message}!")
            time.sleep(wait_time)


if __name__ == "__main__":
    try:
        moon = ToTheMoon()
        moon.main()
    except KeyboardInterrupt:
        sys.exit()
