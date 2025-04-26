#!/usr/bin/env python3
"""
TeamDynamix CLI Utilities

Common utility functions for the TeamDynamix CLI
"""

import os


def clear_screen():
    """Clear the terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")


def format_person_summary(person):
    """Format a person's basic information for display

    Args:
        person (dict): Person data to format

    Returns:
        str: Formatted string with person info
    """
    if not person:
        return "Unknown person"

    name = person.get("FullName", "Unknown")
    email = person.get("PrimaryEmail", "No email")
    uid = person.get("UID", "N/A")

    return f"{name} ({email}) - UID: {uid}"


def display_person_details(person):
    """Display detailed information about a person

    Args:
        person (dict): Person data to display
    """
    if not person:
        print("No person details available.")
        return

    print("\nPerson Details:")
    print("-" * 40)

    # Basic information
    print(f"Name: {person.get('FullName', 'Unknown')}")
    print(f"Email: {person.get('PrimaryEmail', 'No email')}")
    print(f"Username: {person.get('Username', 'N/A')}")
    print(f"UID: {person.get('UID', 'N/A')}")
    print(f"Status: {'Active' if person.get('IsActive') else 'Inactive'}")

    # Additional details if available
    if person.get("Title"):
        print(f"Title: {person['Title']}")
    if person.get("Phone"):
        print(f"Phone: {person['Phone']}")
    if person.get("AlternatePhone"):
        print(f"Alt Phone: {person['AlternatePhone']}")
    if person.get("MobilePhone"):
        print(f"Mobile: {person['MobilePhone']}")
    if person.get("AddressLine1") or person.get("AddressLine2"):
        address = []
        if person.get("AddressLine1"):
            address.append(person["AddressLine1"])
        if person.get("AddressLine2"):
            address.append(person["AddressLine2"])
        if person.get("City"):
            address.append(person["City"])
        if person.get("StateAbbr"):
            address.append(person["StateAbbr"])
        if person.get("PostalCode"):
            address.append(person["PostalCode"])
        print(f"Address: {', '.join(address)}")

    # Show organizational details
    if person.get("OrganizationalID"):
        print(f"Org ID: {person['OrganizationalID']}")
    if person.get("DefaultAccountID"):
        print(f"Default Account ID: {person['DefaultAccountID']}")

    # Show custom attributes if available
    if person.get("Attributes") and len(person["Attributes"]) > 0:
        print("\nCustom Attributes:")
        for attr in person["Attributes"]:
            print(f"  {attr.get('Name', 'Unknown')}: {attr.get('Value', 'N/A')}")

    # Show groups if available
    if person.get("GroupIDs") and len(person["GroupIDs"]) > 0:
        print("\nGroups:")
        for group_id in person["GroupIDs"]:
            print(f"  {group_id}")

    # Show applications if available
    if person.get("Applications") and len(person["Applications"]) > 0:
        print("\nApplications:")
        for app in person["Applications"]:
            # Handle both string values and object values
            if isinstance(app, dict):
                print(f"  {app.get('Name', 'Unknown')}")
            else:
                print(f"  {app}")


def display_people_list(people):
    """Display a list of people with option to select one

    Args:
        people (list): List of people to display

    Returns:
        str: The UID of the selected person, or None if no selection was made
    """
    if not people:
        print("No results found.")
        return None

    print(f"\nFound {len(people)} people:")
    print("-" * 40)

    for i, person in enumerate(people, 1):
        print(
            f"{i}. {person.get('FullName', 'Unknown')} ({person.get('PrimaryEmail', 'No email')})"
        )
        print(f"   UID: {person.get('UID', 'N/A')}")

        # Display additional information if available
        details = []
        if person.get("Title"):
            details.append(f"Title: {person['Title']}")
        if person.get("Phone"):
            details.append(f"Phone: {person['Phone']}")
        if person.get("IsActive") is not None:
            status = "Active" if person["IsActive"] else "Inactive"
            details.append(f"Status: {status}")

        if details:
            print(f"   {' | '.join(details)}")

        print()

    # Prompt for selection
    print("\nEnter a number to view person details, or press Enter to return to menu.")
    selection = input("Select person [1-{}]: ".format(len(people))).strip()

    if selection and selection.isdigit():
        index = int(selection) - 1
        if 0 <= index < len(people):
            return people[index].get("UID")
        else:
            print("Invalid selection.")

    return None
