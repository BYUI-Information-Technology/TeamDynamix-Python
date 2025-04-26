#!/usr/bin/env python3
"""
TeamDynamix API Tickets Commands

Command-line interface commands for Ticket operations
"""

import json
from teamdynamix.utils.cli import clear_screen
from teamdynamix.tickets.display import (
    display_ticket_details,
    display_tickets_list,
    display_feed_entries,
    display_applications,
)


def select_application_command(tickets_client):
    """CLI command to select a ticketing application and present a sub-menu of operations

    Returns:
        str: Selected application ID or None if cancelled
    """
    clear_screen()
    print("Select Ticketing Application")
    print("-" * 40)
    print("DEBUG: Starting application selection process")

    applications = tickets_client.get_applications()
    print(f"DEBUG: Received {len(applications)} applications from API")

    # Debug: Print all applications raw data
    print("DEBUG: Raw application data:")
    for i, app in enumerate(applications):
        print(f"DEBUG: App {i+1}: {app}")

    if not applications:
        print("No ticketing applications found or available to your account.")
        input("\nPress Enter to continue...")
        return None

    # Display the applications and get selection
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

    print(f"DEBUG: User entered selection: '{selection}'")

    app_id = None
    if selection and selection.isdigit():
        index = int(selection) - 1
        if 0 <= index < len(applications):
            app_id = applications[index].get("AppID")
            print(f"DEBUG: Retrieved app_id: {app_id}")
            print(f"DEBUG: App data: {applications[index]}")
        else:
            print("Invalid selection.")
            input("\nPress Enter to continue...")
            return None
    else:
        print("Invalid selection.")
        input("\nPress Enter to continue...")
        return None

    if not app_id or app_id == "N/A":
        print("DEBUG: Application ID is invalid or 'N/A'")
        print(
            "The selected application doesn't have a valid ID. Operations cannot be performed."
        )
        input("\nPress Enter to continue...")
        return None

    if app_id:
        # Display a submenu for this application
        app_name = next(
            (app["Name"] for app in applications if app.get("AppID") == app_id),
            "Unknown",
        )
        print(f"DEBUG: Will show submenu for app_name: {app_name}, app_id: {app_id}")

        try:
            while True:
                clear_screen()
                print(f"Ticketing Application: {app_name} (ID: {app_id})")
                print("-" * 40)
                print("1. Search Tickets")
                print("2. Get Ticket by ID")
                print("3. Create New Ticket")
                print("4. Add Comment to Ticket")
                print("0. Return to Main Menu")
                print()

                sub_choice = input("Select an option [0-4]: ").strip()
                print(f"DEBUG: User selected submenu option: {sub_choice}")

                if sub_choice == "1":
                    print("DEBUG: About to call ticket_search_operation")
                    ticket_search_operation(tickets_client, app_id)
                elif sub_choice == "2":
                    print("DEBUG: About to call ticket_details_operation")
                    ticket_details_operation(tickets_client, app_id)
                elif sub_choice == "3":
                    print("DEBUG: About to call create_ticket_operation")
                    create_ticket_operation(tickets_client, app_id)
                elif sub_choice == "4":
                    print("DEBUG: About to call add_comment_operation")
                    add_comment_operation(tickets_client, app_id)
                elif sub_choice == "0":
                    print("DEBUG: Returning to main menu")
                    return None
                else:
                    print("Invalid selection. Please try again.")
                    input("\nPress Enter to continue...")
        except Exception as e:
            print(f"DEBUG ERROR: An exception occurred in submenu: {str(e)}")
            input("\nPress Enter to continue...")
            return None

    print("DEBUG: Exiting application selection process without valid selection")
    return None


def ticket_search_operation(tickets_client, app_id):
    """Perform ticket search operation for a specific application"""
    clear_screen()
    print("Ticket Search")
    print("-" * 40)
    print(f"Using application ID: {app_id}")

    # Basic search options
    search_params = {}

    # Title search
    title_search = input("Search in title (leave blank to skip): ").strip()
    if title_search:
        search_params["Title"] = title_search

    # Status filter
    status_filter = input("Filter by status (leave blank to skip): ").strip()
    if status_filter:
        search_params["StatusName"] = status_filter

    # Requestor name
    requestor = input("Filter by requestor name (leave blank to skip): ").strip()
    if requestor:
        search_params["RequestorName"] = requestor

    # Ticket ID
    ticket_id = input("Specific ticket ID (leave blank to skip): ").strip()
    if ticket_id:
        try:
            search_params["ID"] = int(ticket_id)
        except ValueError:
            print("Invalid ticket ID. It must be a number.")

    # Maximum results
    max_results = 50
    max_input = input(f"Maximum number of results [default={max_results}]: ").strip()
    if max_input:
        try:
            max_results = int(max_input)
        except ValueError:
            print("Invalid value. Using default.")

    # Add max results to search params
    search_params["MaxResults"] = max_results

    print("\nSearching for tickets...")
    tickets = tickets_client.search_tickets(app_id, search_params)

    if tickets:
        selected_app_id, ticket_id = display_tickets_list(tickets)
        if selected_app_id and ticket_id:
            # Display ticket details
            get_ticket_details_command(tickets_client, selected_app_id, ticket_id)
    else:
        print("No tickets found matching your criteria.")
        input("\nPress Enter to continue...")


def ticket_details_operation(tickets_client, app_id):
    """Get ticket details by ID for a specific application"""
    clear_screen()
    print("Ticket Details")
    print("-" * 40)
    print(f"Using application ID: {app_id}")

    # Get ticket ID
    ticket_id = input("\nEnter ticket ID: ").strip()
    if not ticket_id:
        print("Ticket ID cannot be empty.")
        input("\nPress Enter to continue...")
        return

    # Call the existing get_ticket_details_command function
    get_ticket_details_command(tickets_client, app_id, ticket_id)


def create_ticket_operation(tickets_client, app_id):
    """Create a new ticket for a specific application"""
    clear_screen()
    print("Create New Ticket")
    print("-" * 40)
    print(f"Using application ID: {app_id}")

    # Basic ticket information
    ticket_data = {}

    # Title (required)
    title = input("Ticket Title (required): ").strip()
    if not title:
        print("Title cannot be empty.")
        input("\nPress Enter to continue...")
        return
    ticket_data["Title"] = title

    # Description
    print("\nEnter ticket description (press Enter twice when finished):")
    lines = []
    while True:
        line = input()
        if not line and (not lines or not lines[-1]):
            # Empty line after previous empty line (or at start) means we're done
            break
        lines.append(line)

    description = "\n".join(lines).strip()
    if description:
        ticket_data["Description"] = description

    # Notification options
    notify_requestor = (
        input("\nNotify requestor? (y/n, default=y): ").strip().lower() != "n"
    )
    notify_responsible = (
        input("Notify responsible person/group? (y/n, default=y): ").strip().lower()
        != "n"
    )

    print("\nCreating ticket...")
    new_ticket = tickets_client.create_ticket(
        app_id, ticket_data, notify_requestor, notify_responsible
    )

    if new_ticket:
        print(f"Ticket created successfully! Ticket ID: #{new_ticket.get('ID')}")

        # Option to view created ticket
        view_ticket = input("\nView ticket details? (y/n): ").strip().lower()
        if view_ticket == "y":
            get_ticket_details_command(tickets_client, app_id, new_ticket.get("ID"))
            return
    else:
        print("Failed to create ticket.")

    input("\nPress Enter to continue...")


def add_comment_operation(tickets_client, app_id):
    """Add a comment to a ticket for a specific application"""
    clear_screen()
    print("Add Ticket Comment")
    print("-" * 40)
    print(f"Using application ID: {app_id}")

    # Get ticket ID
    ticket_id = input("\nEnter ticket ID: ").strip()
    if not ticket_id:
        print("Ticket ID cannot be empty.")
        input("\nPress Enter to continue...")
        return

    # Get the comment text
    print("\nEnter your comment (press Enter twice when finished):")
    lines = []
    while True:
        line = input()
        if not line and (not lines or not lines[-1]):
            # Empty line after previous empty line (or at start) means we're done
            break
        lines.append(line)

    comment_text = "\n".join(lines).strip()

    if not comment_text:
        print("Comment cannot be empty.")
        input("\nPress Enter to continue...")
        return

    # Determine if the comment is internal only
    is_internal = (
        input("\nIs this an internal comment (not visible to requestor)? (y/n): ")
        .strip()
        .lower()
        == "y"
    )

    # Create the feed entry
    feed_entry = {
        "Comments": comment_text,
        "IsPrivate": is_internal,
        "IsRichText": False,  # Plain text comment
    }

    print("\nAdding comment to ticket...")
    result = tickets_client.add_feed_entry(app_id, ticket_id, feed_entry)

    if result:
        print("Comment added successfully!")
    else:
        print("Failed to add comment to ticket.")

    input("\nPress Enter to continue...")


def get_ticket_command(tickets_client, app_id=None):
    """CLI command to get detailed information about a ticket by ID"""
    clear_screen()
    print("Ticket Details")
    print("-" * 40)

    # If no app_id is provided, prompt to select one
    if not app_id:
        app_id = select_application_command(tickets_client)
        if not app_id:
            return

    # Now get the ticket ID
    ticket_id = input("\nEnter ticket ID: ").strip()
    if not ticket_id:
        print("Ticket ID cannot be empty.")
        input("\nPress Enter to continue...")
        return

    get_ticket_details_command(tickets_client, app_id, ticket_id)


def get_ticket_details_command(tickets_client, app_id, ticket_id):
    """CLI command to get detailed information about a ticket (without prompting)"""
    if not app_id or not ticket_id:
        return

    print(f"\nRetrieving details for ticket #{ticket_id} in application {app_id}...")

    # Get the ticket details
    ticket = tickets_client.get_ticket(app_id, ticket_id)

    if ticket:
        display_ticket_details(ticket)

        # Offer to show ticket history/feed
        show_history = input("\nShow ticket history/comments? (y/n): ").strip().lower()
        if show_history == "y":
            feed_entries = tickets_client.get_ticket_feed(app_id, ticket_id)
            display_feed_entries(feed_entries)

        # Option to save full JSON to file
        save = input("\nSave full JSON details to file? (y/n): ").lower()
        if save == "y":
            filename = tickets_client.save_ticket_to_file(ticket)
            print(f"Details saved to {filename}")
    else:
        print(f"Could not retrieve details for ticket #{ticket_id}")

    input("\nPress Enter to continue...")


def search_tickets_command(tickets_client, app_id=None):
    """CLI command to search for tickets"""
    clear_screen()
    print("Ticket Search")
    print("-" * 40)

    # If no app_id is provided, prompt to select one
    if not app_id:
        app_id = select_application_command(tickets_client)
        if not app_id:
            return

    # Display selected application ID
    print(f"Using application ID: {app_id}")

    # Basic search options
    search_params = {}

    # Title search
    title_search = input("Search in title (leave blank to skip): ").strip()
    if title_search:
        search_params["Title"] = title_search

    # Status filter
    status_filter = input("Filter by status (leave blank to skip): ").strip()
    if status_filter:
        search_params["StatusName"] = status_filter

    # Requestor name
    requestor = input("Filter by requestor name (leave blank to skip): ").strip()
    if requestor:
        search_params["RequestorName"] = requestor

    # Ticket ID
    ticket_id = input("Specific ticket ID (leave blank to skip): ").strip()
    if ticket_id:
        try:
            search_params["ID"] = int(ticket_id)
        except ValueError:
            print("Invalid ticket ID. It must be a number.")

    # Maximum results
    max_results = 50
    max_input = input(f"Maximum number of results [default={max_results}]: ").strip()
    if max_input:
        try:
            max_results = int(max_input)
        except ValueError:
            print("Invalid value. Using default.")

    # Add max results to search params
    search_params["MaxResults"] = max_results

    print("\nSearching for tickets...")
    tickets = tickets_client.search_tickets(app_id, search_params)

    if tickets:
        selected_app_id, ticket_id = display_tickets_list(tickets)
        if selected_app_id and ticket_id:
            get_ticket_details_command(tickets_client, selected_app_id, ticket_id)
    else:
        print("No tickets found matching your criteria.")
        input("\nPress Enter to continue...")


def create_ticket_comment_command(tickets_client, app_id=None):
    """CLI command to add a comment to a ticket"""
    clear_screen()
    print("Add Ticket Comment")
    print("-" * 40)

    # If no app_id is provided, prompt to select one
    if not app_id:
        app_id = select_application_command(tickets_client)
        if not app_id:
            return

    # Display selected application ID
    print(f"Using application ID: {app_id}")

    # Now get the ticket ID
    ticket_id = input("\nEnter ticket ID: ").strip()
    if not ticket_id:
        print("Ticket ID cannot be empty.")
        input("\nPress Enter to continue...")
        return

    # Get the comment text
    print("\nEnter your comment (press Enter twice when finished):")
    lines = []
    while True:
        line = input()
        if not line and (not lines or not lines[-1]):
            # Empty line after previous empty line (or at start) means we're done
            break
        lines.append(line)

    comment_text = "\n".join(lines).strip()

    if not comment_text:
        print("Comment cannot be empty.")
        input("\nPress Enter to continue...")
        return

    # Determine if the comment is internal only
    is_internal = (
        input("\nIs this an internal comment (not visible to requestor)? (y/n): ")
        .strip()
        .lower()
        == "y"
    )

    # Create the feed entry
    feed_entry = {
        "Comments": comment_text,
        "IsPrivate": is_internal,
        "IsRichText": False,  # Plain text comment
    }

    print("\nAdding comment to ticket...")
    result = tickets_client.add_feed_entry(app_id, ticket_id, feed_entry)

    if result:
        print("Comment added successfully!")
    else:
        print("Failed to add comment to ticket.")

    input("\nPress Enter to continue...")


def create_ticket_command(tickets_client, app_id=None):
    """CLI command to create a new ticket"""
    clear_screen()
    print("Create New Ticket")
    print("-" * 40)

    # If no app_id is provided, prompt to select one
    if not app_id:
        app_id = select_application_command(tickets_client)
        if not app_id:
            return

    # Display selected application ID
    print(f"Using application ID: {app_id}")

    # Basic ticket information
    ticket_data = {}

    # Title (required)
    title = input("Ticket Title (required): ").strip()
    if not title:
        print("Title cannot be empty.")
        input("\nPress Enter to continue...")
        return
    ticket_data["Title"] = title

    # Description
    print("\nEnter ticket description (press Enter twice when finished):")
    lines = []
    while True:
        line = input()
        if not line and (not lines or not lines[-1]):
            # Empty line after previous empty line (or at start) means we're done
            break
        lines.append(line)

    description = "\n".join(lines).strip()
    if description:
        ticket_data["Description"] = description

    # Notification options
    notify_requestor = (
        input("\nNotify requestor? (y/n, default=y): ").strip().lower() != "n"
    )
    notify_responsible = (
        input("Notify responsible person/group? (y/n, default=y): ").strip().lower()
        != "n"
    )

    print("\nCreating ticket...")
    new_ticket = tickets_client.create_ticket(
        app_id, ticket_data, notify_requestor, notify_responsible
    )

    if new_ticket:
        print(f"Ticket created successfully! Ticket ID: #{new_ticket.get('ID')}")

        # Option to view created ticket
        view_ticket = input("\nView ticket details? (y/n): ").strip().lower()
        if view_ticket == "y":
            get_ticket_details_command(tickets_client, app_id, new_ticket.get("ID"))
            return
    else:
        print("Failed to create ticket.")

    input("\nPress Enter to continue...")
