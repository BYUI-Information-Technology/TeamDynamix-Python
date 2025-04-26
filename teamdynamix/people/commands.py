#!/usr/bin/env python3
"""
TeamDynamix API People Commands

Command-line interface commands for People operations
"""

import json
from teamdynamix.utils.cli import (
    clear_screen,
    display_person_details,
    display_people_list,
)


def search_people_command(people_client):
    """CLI command to search for people in TeamDynamix"""
    clear_screen()
    print("Person Lookup")
    print("-" * 40)

    search_text = input("Enter search text (name, email, etc.): ").strip()
    if not search_text:
        print("Search text cannot be empty.")
        input("\nPress Enter to continue...")
        return

    max_results = 50
    max_input = input(
        f"Maximum number of results [1-100, default={max_results}]: "
    ).strip()
    if max_input:
        try:
            max_results = int(max_input)
            if max_results < 1 or max_results > 100:
                print("Value must be between 1 and 100. Using default.")
                max_results = 50
        except ValueError:
            print("Invalid value. Using default.")

    print(f"\nSearching for people matching '{search_text}'...")

    # Call the client to search for people
    people = people_client.search_people(search_text, max_results)

    if people:
        selected_uid = display_people_list(people)
        if selected_uid:
            get_person_details_by_uid_command(people_client, selected_uid)
    else:
        print("No results found.")

    input("\nPress Enter to continue...")


def get_person_details_command(people_client):
    """CLI command to get detailed information about a person by UID"""
    clear_screen()
    print("Person Details")
    print("-" * 40)

    uid = input("Enter person UID: ").strip()
    if not uid:
        print("UID cannot be empty.")
        input("\nPress Enter to continue...")
        return

    get_person_details_by_uid_command(people_client, uid)


def get_person_details_by_uid_command(people_client, uid):
    """CLI command to get detailed information about a person by UID (without prompting)"""
    if not uid:
        return

    print(f"\nRetrieving details for person with UID: {uid}...")

    # Call the client to get person details
    person = people_client.get_person_by_uid(uid)

    if person:
        display_person_details(person)

        # Option to save full JSON to file
        save = input("\nSave full JSON details to file? (y/n): ").lower()
        if save == "y":
            filename = people_client.save_person_to_file(person)
            print(f"Details saved to {filename}")
    else:
        print(f"Could not retrieve details for person with UID {uid}")

    input("\nPress Enter to continue...")


def get_person_by_username_command(people_client):
    """CLI command to get person information by username"""
    clear_screen()
    print("Person Lookup by Username")
    print("-" * 40)

    username = input("Enter username: ").strip()
    if not username:
        print("Username cannot be empty.")
        input("\nPress Enter to continue...")
        return

    print(f"\nRetrieving details for person with username: {username}...")

    # Call the client to get person by username
    person = people_client.get_person_by_username(username)

    if person:
        display_person_details(person)

        # Option to save full JSON to file
        save = input("\nSave full JSON details to file? (y/n): ").lower()
        if save == "y":
            filename = people_client.save_person_to_file(person)
            print(f"Details saved to {filename}")
    else:
        print(f"Could not retrieve details for person with username {username}")

    input("\nPress Enter to continue...")


def get_uid_by_username_command(people_client):
    """CLI command to get person's UID by their username"""
    clear_screen()
    print("Get UID by Username")
    print("-" * 40)

    username = input("Enter username: ").strip()
    if not username:
        print("Username cannot be empty.")
        input("\nPress Enter to continue...")
        return

    print(f"\nRetrieving UID for person with username: {username}...")

    # Call the client to get UID by username
    uid = people_client.get_uid_by_username(username)

    if uid:
        print(f"\nUsername: {username}")
        print(f"UID: {uid}")
    else:
        print(f"Could not retrieve UID for username {username}")

    input("\nPress Enter to continue...")
