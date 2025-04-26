#!/usr/bin/env python3
"""
TeamDynamix Ticket Display Functions

Functions for displaying ticket information in the CLI
"""

import datetime


def format_ticket_summary(ticket):
    """Format a ticket's basic information for display

    Args:
        ticket (dict): Ticket data to format

    Returns:
        str: Formatted string with ticket info
    """
    if not ticket:
        return "Unknown ticket"

    ticket_id = ticket.get("ID", "N/A")
    title = ticket.get("Title", "Untitled")
    status = ticket.get("StatusName", "Unknown Status")

    return f"#{ticket_id} - {title} ({status})"


def display_ticket_details(ticket):
    """Display detailed information about a ticket

    Args:
        ticket (dict): Ticket data to display
    """
    if not ticket:
        print("No ticket details available.")
        return

    print("\nTicket Details:")
    print("-" * 40)

    # Basic information
    print(f"Ticket ID: #{ticket.get('ID', 'N/A')}")
    print(f"Title: {ticket.get('Title', 'Untitled')}")
    print(f"Status: {ticket.get('StatusName', 'Unknown')}")
    print(f"Priority: {ticket.get('PriorityName', 'Unknown')}")

    # Dates
    created_date = ticket.get("CreatedDate")
    if created_date:
        # Convert from "/Date(1234567890000)/" format if needed
        if isinstance(created_date, str) and created_date.startswith("/Date("):
            timestamp = int(created_date[6:-2]) / 1000
            created_date = datetime.datetime.fromtimestamp(timestamp).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        print(f"Created: {created_date}")

    # People
    if ticket.get("RequestorName"):
        print(f"Requestor: {ticket.get('RequestorName')}")
    if ticket.get("ResponsibleGroupName"):
        print(f"Responsible Group: {ticket.get('ResponsibleGroupName')}")
    if ticket.get("ResponsibleName"):
        print(f"Responsible: {ticket.get('ResponsibleName')}")

    # Additional details
    if ticket.get("Description"):
        print("\nDescription:")
        print("-" * 40)
        print(ticket.get("Description"))

    # Custom attributes if available
    if ticket.get("Attributes") and len(ticket["Attributes"]) > 0:
        print("\nCustom Attributes:")
        for attr in ticket["Attributes"]:
            print(f"  {attr.get('Name', 'Unknown')}: {attr.get('Value', 'N/A')}")


def display_tickets_list(tickets):
    """Display a list of tickets with option to select one

    Args:
        tickets (list): List of tickets to display

    Returns:
        tuple: (app_id, ticket_id) of selected ticket, or (None, None) if no selection
    """
    if not tickets:
        print("No tickets found.")
        return None, None

    print(f"\nFound {len(tickets)} tickets:")
    print("-" * 40)

    for i, ticket in enumerate(tickets, 1):
        app_id = ticket.get("AppID", "N/A")
        ticket_id = ticket.get("ID", "N/A")
        title = ticket.get("Title", "Untitled")
        status = ticket.get("StatusName", "Unknown Status")
        priority = ticket.get("PriorityName", "Unknown Priority")

        print(f"{i}. #{ticket_id} - {title}")
        print(f"   Status: {status} | Priority: {priority} | App ID: {app_id}")
        print()

    # Prompt for selection
    print("\nEnter a number to view ticket details, or press Enter to return to menu.")
    selection = input("Select ticket [1-{}]: ".format(len(tickets))).strip()

    if selection and selection.isdigit():
        index = int(selection) - 1
        if 0 <= index < len(tickets):
            app_id = tickets[index].get("AppID")
            ticket_id = tickets[index].get("ID")
            return app_id, ticket_id
        else:
            print("Invalid selection.")

    return None, None


def display_feed_entries(feed_entries):
    """Display feed entries (comments/updates) for a ticket

    Args:
        feed_entries (list): List of feed entries to display
    """
    if not feed_entries:
        print("No comments or updates found.")
        return

    print(f"\nTicket History ({len(feed_entries)} entries):")
    print("-" * 40)

    # Sort entries by created date if available
    sorted_entries = sorted(
        feed_entries,
        key=lambda x: x.get("CreatedDate", "0") if x.get("CreatedDate") else "0",
        reverse=True,
    )

    for entry in sorted_entries:
        # Get creator information
        creator = entry.get("CreatedByName", "Unknown")

        # Get date information
        created_date = entry.get("CreatedDate")
        if (
            created_date
            and isinstance(created_date, str)
            and created_date.startswith("/Date(")
        ):
            timestamp = int(created_date[6:-2]) / 1000
            created_date = datetime.datetime.fromtimestamp(timestamp).strftime(
                "%Y-%m-%d %H:%M:%S"
            )

        # Entry type and content
        entry_type = entry.get("TypeName", "Comment")
        comments = entry.get("Comments", "")

        print(f"{created_date} - {creator} ({entry_type})")
        if comments:
            # Indent comment lines
            indented_comments = "\n".join(
                ["    " + line for line in comments.split("\n")]
            )
            print(indented_comments)
        print()


def display_applications(applications):
    """Display available ticketing applications with option to select one

    Args:
        applications (list): List of applications to display

    Returns:
        str: ID of selected application, or None if no selection
    """
    if not applications:
        print("No ticketing applications found.")
        return None

    print(f"\nFound {len(applications)} ticketing applications:")
    print("-" * 40)

    for i, app in enumerate(applications, 1):
        app_id = app.get("AppID", "N/A")
        name = app.get("Name", "Unknown")

        print(f"{i}. {name} (ID: {app_id})")

    # Prompt for selection
    print("\nSelect an application to use (or enter 'q' to return to main menu):")
    selection = input(f"Select application [1-{len(applications)}]: ").strip()

    # Add option to quit
    if selection.lower() == "q":
        return None

    if selection and selection.isdigit():
        index = int(selection) - 1
        if 0 <= index < len(applications):
            app_id = applications[index].get("AppID")

            # Handle the case where ID is "N/A"
            if app_id == "N/A":
                print(
                    "The selected application doesn't have a valid ID. Operations cannot be performed."
                )
                input("\nPress Enter to continue...")
                return None

            return app_id
        else:
            print("Invalid selection.")

    return None
