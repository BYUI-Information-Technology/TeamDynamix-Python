#!/usr/bin/env python3
"""
TeamDynamix API People Module

Handles operations related to people in TeamDynamix
"""

import json
import urllib.parse


class PeopleClient:
    """Client for people-related operations in TeamDynamix API"""

    def __init__(self, auth):
        """Initialize with authentication client"""
        self.auth = auth

    def search_people(self, search_text, max_results=50):
        """Search for people in TeamDynamix

        Args:
            search_text (str): Text to search for (name, email, etc.)
            max_results (int): Maximum number of results to return (1-100)

        Returns:
            list: List of people matching the search criteria
        """
        if not search_text:
            return []

        if max_results < 1 or max_results > 100:
            max_results = 50

        # URL encode the search text to handle special characters
        encoded_search = urllib.parse.quote(search_text)

        # Construct the endpoint URL with query parameters
        endpoint = (
            f"api/people/lookup?searchText={encoded_search}&maxResults={max_results}"
        )

        # Make the API request
        response = self.auth.make_api_request("GET", endpoint)

        if response and response.status_code == 200:
            return response.json()
        else:
            print("Error performing person lookup")
            if response:
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text[:200]}...")
            return []

    def get_person_by_uid(self, uid):
        """Get detailed information about a person by UID

        Args:
            uid (str): The UID of the person to retrieve

        Returns:
            dict: Person details or None if not found
        """
        if not uid:
            return None

        # Construct the endpoint URL
        endpoint = f"api/people/{uid}"

        # Make the API request
        response = self.auth.make_api_request("GET", endpoint)

        if response and response.status_code == 200:
            return response.json()
        else:
            print(f"Error retrieving person with UID {uid}")
            if response:
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text[:200]}...")
            return None

    def get_person_by_username(self, username):
        """Get person information by username

        Args:
            username (str): The username to look up

        Returns:
            dict: Person details or None if not found
        """
        if not username:
            return None

        # Construct the endpoint URL
        endpoint = f"api/people/{username}"

        # Make the API request
        response = self.auth.make_api_request("GET", endpoint)

        if response and response.status_code == 200:
            return response.json()
        else:
            print(f"Error retrieving person with username {username}")
            if response:
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text[:200]}...")
            return None

    def get_uid_by_username(self, username):
        """Get person's UID by their username

        Args:
            username (str): The username to look up

        Returns:
            str: The UID of the person or None if not found
        """
        if not username:
            return None

        # Construct the endpoint URL
        endpoint = f"api/people/getuid/{username}"

        # Make the API request
        response = self.auth.make_api_request("GET", endpoint)

        if response and response.status_code == 200:
            return response.text.strip('"')  # API returns the UID as a JSON string
        else:
            print(f"Error retrieving UID for username {username}")
            if response:
                print(f"Status code: {response.status_code}")
                print(f"Response: {response.text[:200]}...")
            return None

    def save_person_to_file(self, person, filename=None):
        """Save person details to a JSON file

        Args:
            person (dict): The person details to save
            filename (str, optional): Custom filename to use

        Returns:
            str: The filename where the data was saved
        """
        if not person:
            return None

        if not filename:
            filename = f"person_{person.get('UID', 'unknown')}.json"

        with open(filename, "w") as f:
            json.dump(person, f, indent=2)

        return filename
