#!/usr/bin/env python3
"""
TeamDynamix API Tickets Module

Handles operations related to tickets in TeamDynamix
"""

import json
import urllib.parse


class TicketsClient:
    """Client for tickets-related operations in TeamDynamix API"""

    def __init__(self, auth):
        """Initialize with authentication client"""
        self.auth = auth

    def get_ticket(self, app_id, ticket_id):
        """Get detailed information about a ticket by ID

        Args:
            app_id (str): The application ID
            ticket_id (str): The ticket ID to retrieve

        Returns:
            dict: Ticket details or None if not found
        """
        if not app_id or not ticket_id:
            return None

        # Construct the endpoint URL
        endpoint = f"api/{app_id}/tickets/{ticket_id}"

        # Make the API request
        response = self.auth.make_api_request("GET", endpoint)

        if response and response.status_code == 200:
            return response.json()
        else:
            print(f"Error retrieving ticket with ID {ticket_id}")
            if response:
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text[:200]}...")
            return None

    def search_tickets(self, app_id, search_params=None):
        """Search for tickets with given parameters

        Args:
            app_id (str): The application ID
            search_params (dict): Parameters for ticket search

        Returns:
            list: List of tickets matching the search criteria
        """
        if not app_id:
            return []

        if not search_params:
            search_params = {}

        # Construct the endpoint URL
        endpoint = f"api/{app_id}/tickets/search"

        # Make the API request with search parameters in the body
        response = self.auth.make_api_request("POST", endpoint, json=search_params)

        if response and response.status_code == 200:
            return response.json()
        else:
            print("Error performing ticket search")
            if response:
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text[:200]}...")
            return []

    def create_ticket(
        self, app_id, ticket_data, notify_requestor=True, notify_responsible=True
    ):
        """Create a new ticket

        Args:
            app_id (str): The application ID
            ticket_data (dict): The ticket data to submit
            notify_requestor (bool): Whether to notify the requestor
            notify_responsible (bool): Whether to notify the responsible resource

        Returns:
            dict: The created ticket or None if failed
        """
        if not app_id or not ticket_data:
            return None

        # Construct the endpoint URL with query parameters
        endpoint = f"api/{app_id}/tickets?NotifyRequestor={str(notify_requestor).lower()}&NotifyResponsible={str(notify_responsible).lower()}"

        # Make the API request
        response = self.auth.make_api_request("POST", endpoint, json=ticket_data)

        if response and response.status_code == 201:  # 201 Created
            return response.json()
        else:
            print("Error creating ticket")
            if response:
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text[:200]}...")
            return None

    def update_ticket(
        self, app_id, ticket_id, ticket_data, notify_new_responsible=True
    ):
        """Update an existing ticket

        Args:
            app_id (str): The application ID
            ticket_id (str): The ticket ID to update
            ticket_data (dict): The updated ticket data
            notify_new_responsible (bool): Whether to notify new responsible resources

        Returns:
            dict: The updated ticket or None if failed
        """
        if not app_id or not ticket_id or not ticket_data:
            return None

        # Construct the endpoint URL
        endpoint = f"api/{app_id}/tickets/{ticket_id}?notifyNewResponsible={str(notify_new_responsible).lower()}"

        # Make the API request
        response = self.auth.make_api_request("POST", endpoint, json=ticket_data)

        if response and response.status_code == 200:
            return response.json()
        else:
            print(f"Error updating ticket with ID {ticket_id}")
            if response:
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text[:200]}...")
            return None

    def get_ticket_statuses(self, app_id):
        """Get available ticket statuses for the application

        Args:
            app_id (str): The application ID

        Returns:
            list: Available ticket statuses
        """
        if not app_id:
            return []

        # Construct the endpoint URL
        endpoint = f"api/{app_id}/tickets/statuses"

        # Make the API request
        response = self.auth.make_api_request("GET", endpoint)

        if response and response.status_code == 200:
            return response.json()
        else:
            print("Error retrieving ticket statuses")
            if response:
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text[:200]}...")
            return []

    def get_ticket_feed(self, app_id, ticket_id):
        """Get feed entries (comments/updates) for a ticket

        Args:
            app_id (str): The application ID
            ticket_id (str): The ticket ID

        Returns:
            list: Feed entries for the ticket
        """
        if not app_id or not ticket_id:
            return []

        # Construct the endpoint URL
        endpoint = f"api/{app_id}/tickets/{ticket_id}/feed"

        # Make the API request
        response = self.auth.make_api_request("GET", endpoint)

        if response and response.status_code == 200:
            return response.json()
        else:
            print(f"Error retrieving feed for ticket with ID {ticket_id}")
            if response:
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text[:200]}...")
            return []

    def add_feed_entry(self, app_id, ticket_id, feed_entry):
        """Add a comment or update to a ticket's feed

        Args:
            app_id (str): The application ID
            ticket_id (str): The ticket ID
            feed_entry (dict): The feed entry data

        Returns:
            dict: The created feed entry or None if failed
        """
        if not app_id or not ticket_id or not feed_entry:
            return None

        # Construct the endpoint URL
        endpoint = f"api/{app_id}/tickets/{ticket_id}/feed"

        # Make the API request
        response = self.auth.make_api_request("POST", endpoint, json=feed_entry)

        if response and response.status_code == 200:
            return response.json()
        else:
            print(f"Error adding feed entry to ticket with ID {ticket_id}")
            if response:
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text[:200]}...")
            return None

    def get_applications(self):
        """Get available ticketing applications

        Returns:
            list: Available ticketing applications
        """
        print("DEBUG: Calling get_applications method")

        # Construct the endpoint URL
        endpoint = "api/applications"
        print(f"DEBUG: Using endpoint: {endpoint}")

        # Make the API request
        response = self.auth.make_api_request("GET", endpoint)

        if response:
            print(f"DEBUG: Response status: {response.status_code}")
            print(f"DEBUG: Response headers: {response.headers}")
        else:
            print("DEBUG: No response received from API")

        if response and response.status_code == 200:
            apps = response.json()
            print(f"DEBUG: Received {len(apps)} total applications")

            # Filter to only include ticketing applications
            ticketing_apps = [app for app in apps if app.get("AppClass") == "TDTickets"]
            print(f"DEBUG: Filtered to {len(ticketing_apps)} ticketing applications")

            # Additional debug: print first app in detail
            if ticketing_apps:
                print(f"DEBUG: First app details: {ticketing_apps[0]}")

            return ticketing_apps
        else:
            print("Error retrieving applications")
            if response:
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text[:200]}...")
            return []

    def save_ticket_to_file(self, ticket, filename=None):
        """Save ticket details to a JSON file

        Args:
            ticket (dict): The ticket details to save
            filename (str, optional): Custom filename to use

        Returns:
            str: The filename where the data was saved
        """
        if not ticket:
            return None

        if not filename:
            filename = f"ticket_{ticket.get('ID', 'unknown')}.json"

        with open(filename, "w") as f:
            json.dump(ticket, f, indent=2)

        return filename
