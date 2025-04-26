#!/usr/bin/env python3
"""
TeamDynamix API Authentication Module

Handles authentication and environment selection for the TeamDynamix API
"""

import os
from archive.teamdynamix_auth import TeamDynamixAuth


class AuthClient:
    """Authentication client for TeamDynamix API"""

    @staticmethod
    def select_environment():
        """Prompt user to select an environment"""
        print("TeamDynamix API Environment Selection")
        print("-" * 40)
        print("1. Sandbox")
        print("2. Production")
        print()

        while True:
            choice = input("Select environment [1-2]: ").strip()
            if choice == "1":
                return "sandbox"
            elif choice == "2":
                return "production"
            else:
                print("Invalid selection. Please try again.")

    @staticmethod
    def authenticate(environment):
        """Authenticate to the TeamDynamix API"""
        auth = TeamDynamixAuth(environment=environment)
        print(f"\nUsing TeamDynamix API at: {auth.base_url}")

        print("\nAuthenticating...", end="", flush=True)
        if auth.login():
            print(" Success!")
            user_info = auth.get_current_user()
            if user_info:
                print(f"Logged in as: {user_info.get('FullName', 'Unknown')}")
            print(f"Token expires at: {auth.token_expiry}")
            return auth
        else:
            print(" Failed!")
            print("Authentication failed. Please check your credentials.")
            return None
