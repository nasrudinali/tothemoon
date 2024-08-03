import sys

sys.dont_write_bytecode = True

from package import base
from package.core.token import get_token
from package.core.info import asset
from package.core.check_in import process_check_in
from package.core.do_task import process_do_task
from package.core.claim_invite import process_claim_invite
from package.core.explore_planet import process_explore_planet
from package.core.farm import process_farming

import time
import brotli


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

                try:
                    # Get token
                    token = get_token(data=data)

                    if token:
                        # Get game info
                        sd, probe, eth, invite_sd, farm_end_time, current_time = asset(
                            token=token
                        )
                        base.log(
                            f"{base.green}SD: {base.white}{sd} - {base.green}Probe: {base.white}{probe} - {base.green}ETH: {base.white}{eth}"
                        )

                        # Check in
                        if self.auto_check_in:
                            base.log(f"{base.yellow}Auto Check-in: {base.green}ON")
                            process_check_in(token=token)
                        else:
                            base.log(f"{base.yellow}Auto Check-in: {base.red}OFF")

                        # Do task
                        if self.auto_do_task:
                            base.log(f"{base.yellow}Auto Do Task: {base.green}ON")
                            process_do_task(token=token)
                        else:
                            base.log(f"{base.yellow}Auto Do Task: {base.red}OFF")

                        # Claim invite
                        if self.auto_claim_invite:
                            base.log(f"{base.yellow}Auto Claim Invite: {base.green}ON")
                            if invite_sd > 0:
                                process_claim_invite(token=token)
                            else:
                                base.log(
                                    f"{base.white}Claim Invite: {base.red}No SD from friends"
                                )
                        else:
                            base.log(f"{base.yellow}Auto Claim Invite: {base.red}OFF")

                        # Explore planet
                        if self.auto_explore_planet:
                            base.log(
                                f"{base.yellow}Auto Explore Planet: {base.green}ON"
                            )
                            if probe > 0:
                                process_explore_planet(token=token)
                            else:
                                base.log(
                                    f"{base.white}Explore Planet: {base.red}No Probe available"
                                )
                        else:
                            base.log(f"{base.yellow}Auto Explore Planet: {base.red}OFF")

                        # Farming
                        if self.auto_farm:
                            base.log(f"{base.yellow}Auto Farm: {base.green}ON")
                            if farm_end_time == 0:
                                time_left = process_farming(token=token)
                                time_left_list.append(time_left)
                            else:
                                base.log(
                                    f"{base.white}Auto Farm: {base.red}Not time to claim yet"
                                )
                                time_left = (farm_end_time - current_time) / 1000
                                time_left_list.append(time_left)
                        else:
                            base.log(f"{base.yellow}Auto Farm: {base.red}OFF")

                    else:
                        base.log(f"{base.red}Token not found! Please get new query id")
                except Exception as e:
                    base.log(f"{base.red}Error: {base.white}{e}")

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
