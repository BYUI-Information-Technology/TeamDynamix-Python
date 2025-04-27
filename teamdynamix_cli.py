#!/usr/bin/env python3
"""
TeamDynamix API Command Line Interface

An interactive CLI for working with the TeamDynamix API
"""
import os
import sys
from dotenv import load_dotenv
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Import modules from the package
from teamdynamix.auth.client import AuthClient
from teamdynamix.people.client import PeopleClient
from teamdynamix.tickets.client import TicketsClient
from teamdynamix.people.commands import (
    search_people_command,
    get_person_details_command,
    get_person_by_username_command,
    get_uid_by_username_command,
)
from teamdynamix.tickets.commands import (
    search_tickets_command,
    get_ticket_command,
    create_ticket_command,
    create_ticket_comment_command,
    select_application_command,
)
from teamdynamix.utils.cli import (
    clear_screen,
    display_title,
    divider,
    box,
    display_pixelated_tdx,
    display_bordered_ascii,
)


def main_menu(auth):
    """Display the main menu and handle user selection"""
    # Initialize clients
    people_client = PeopleClient(auth)
    tickets_client = TicketsClient(auth)

    while True:
        clear_screen()
        display_bordered_ascii()

        # Status information in a box
        user_info = auth.get_current_user()
        user_name = "Unknown"
        if user_info:
            user_name = user_info.get("FullName", "Unknown")

        status_info = (
            f"Environment: {auth.environment.title()}\n"
            f"API URL: {auth.base_url}\n"
            f"User: {user_name}"
        )
        print(
            f"{Fore.CYAN}{box(status_info, width=60, style='rounded')}{Style.RESET_ALL}"
        )
        print()

        # Menu options
        print(f"{Fore.MAGENTA}{Style.BRIGHT}PEOPLE OPERATIONS:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}1. {Fore.LIGHTBLUE_EX}Search for People{Style.RESET_ALL}")
        print(
            f"{Fore.WHITE}2. {Fore.LIGHTBLUE_EX}Get Person Details by UID{Style.RESET_ALL}"
        )
        print(
            f"{Fore.WHITE}3. {Fore.LIGHTBLUE_EX}Get Person Details by Username{Style.RESET_ALL}"
        )
        print(f"{Fore.WHITE}4. {Fore.LIGHTBLUE_EX}Get UID by Username{Style.RESET_ALL}")
        print()
        print(f"{Fore.MAGENTA}{Style.BRIGHT}TICKET OPERATIONS:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}5. {Fore.LIGHTBLUE_EX}Ticket Operations{Style.RESET_ALL}")
        print()
        print(f"{Fore.MAGENTA}{Style.BRIGHT}SYSTEM:{Style.RESET_ALL}")
        print(f"{Fore.WHITE}S. {Fore.LIGHTBLUE_EX}Switch Environment{Style.RESET_ALL}")
        print(f"{Fore.WHITE}X. {Fore.LIGHTBLUE_EX}Exit{Style.RESET_ALL}")
        print()

        choice = (
            input(f"{Fore.GREEN}Select an option: {Style.RESET_ALL}").strip().lower()
        )

        # People operations
        if choice == "1":
            search_people_command(people_client)
        elif choice == "2":
            get_person_details_command(people_client)
        elif choice == "3":
            get_person_by_username_command(people_client)
        elif choice == "4":
            get_uid_by_username_command(people_client)

        # Ticket operations
        elif choice == "5":
            select_application_command(tickets_client)

        # System operations
        elif choice == "s":
            return True  # Signal to switch environment
        elif choice == "x":
            return False  # Signal to exit
        else:
            print(f"{Fore.RED}Invalid selection. Please try again.{Style.RESET_ALL}")
            input(f"\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")


def main():
    """Main entry point for the CLI"""
    # Load environment variables
    load_dotenv()

    # Welcome message
    clear_screen()
    display_bordered_ascii()
    welcome_text = "Welcome to TDX Python CLI. This tool allows you to interact with the TeamDynamix API."
    print(f"{Fore.CYAN}{box(welcome_text, width=60, style='double')}{Style.RESET_ALL}")
    print()

    switch_env = True
    while switch_env:
        # Select environment
        environment = AuthClient.select_environment()

        # Authenticate
        auth = AuthClient.authenticate(environment)
        if not auth:
            input(f"\n{Fore.YELLOW}Press Enter to try again...{Style.RESET_ALL}")
            continue

        # Show main menu
        switch_env = main_menu(auth)

    # Goodbye message
    clear_screen()
    display_bordered_ascii()
    goodbye_text = "Thank you for using TDX Python CLI. Goodbye!"
    print(f"{Fore.CYAN}{box(goodbye_text, width=60, style='rounded')}{Style.RESET_ALL}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
