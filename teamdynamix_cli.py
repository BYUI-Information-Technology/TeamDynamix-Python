#!/usr/bin/env python3
"""
TeamDynamix API Command Line Interface

An interactive CLI for working with the TeamDynamix API
"""
import os
import sys
from dotenv import load_dotenv

# Import modules from the package
from teamdynamix.auth.client import AuthClient
from teamdynamix.people.client import PeopleClient
from teamdynamix.people.commands import (
    search_people_command,
    get_person_details_command,
    get_person_by_username_command,
    get_uid_by_username_command,
)
from teamdynamix.utils.cli import clear_screen


def main_menu(auth):
    """Display the main menu and handle user selection"""
    # Initialize clients
    people_client = PeopleClient(auth)

    while True:
        clear_screen()
        print("TeamDynamix API Tool")
        print("-" * 40)
        print(f"Environment: {auth.environment.title()}")
        print(f"API URL: {auth.base_url}")

        # Get current user info, handle case where it might be None
        user_info = auth.get_current_user()
        user_name = "Unknown"
        if user_info:
            user_name = user_info.get("FullName", "Unknown")
        print(f"User: {user_name}")

        print("-" * 40)
        print("1. Search for People")
        print("2. Get Person Details by UID")
        print("3. Get Person Details by Username")
        print("4. Get UID by Username")
        print("5. Switch Environment")
        print("0. Exit")
        print()

        choice = input("Select an option [0-5]: ").strip()

        if choice == "1":
            search_people_command(people_client)
        elif choice == "2":
            get_person_details_command(people_client)
        elif choice == "3":
            get_person_by_username_command(people_client)
        elif choice == "4":
            get_uid_by_username_command(people_client)
        elif choice == "5":
            return True  # Signal to switch environment
        elif choice == "0":
            return False  # Signal to exit
        else:
            print("Invalid selection. Please try again.")
            input("\nPress Enter to continue...")


def main():
    """Main entry point for the CLI"""
    # Load environment variables
    load_dotenv()

    # Welcome message
    clear_screen()
    print("Welcome to TeamDynamix API Tool")
    print("=" * 40)
    print("This tool allows you to interact with the TeamDynamix API.")
    print()

    switch_env = True
    while switch_env:
        # Select environment
        environment = AuthClient.select_environment()

        # Authenticate
        auth = AuthClient.authenticate(environment)
        if not auth:
            input("\nPress Enter to try again...")
            continue

        # Show main menu
        switch_env = main_menu(auth)

    # Goodbye message
    clear_screen()
    print("Thank you for using TeamDynamix API Tool")
    print("=" * 40)
    return 0


if __name__ == "__main__":
    sys.exit(main())
