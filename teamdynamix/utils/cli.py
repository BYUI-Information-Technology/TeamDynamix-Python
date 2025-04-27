#!/usr/bin/env python3
"""
TeamDynamix CLI Utilities

Common utility functions for the TeamDynamix CLI
"""

import os
import random
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)


def clear_screen():
    """Clear the terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")


# ASCII Art Title
def display_title(style="default"):
    """Display an ASCII art title for TeamDynamix CLI

    Args:
        style (str): Style of ASCII art to display. Options are 'default', 'slim', 'azure', 'random'
    """
    if style == "random":
        style = random.choice(["default", "slim", "azure"])

    if style == "slim":
        lines = [
            "╔╦╗╔╦╗═╗ ╦  ╔═╗┬ ┬┌┬┐┬ ┬┌─┐┌┐┌  ╔═╗╦  ╦",
            " ║  ║║╔╩╦╝  ╠═╝└┬┘ │ ├─┤│ ││││  ║  │  │",
            " ╩ ═╩╝╩ ╚═  ╩   ┴  ┴ ┴ ┴└─┘┘└┘  ╚═╝┴─┘┴",
        ]
        # Print with cyan coloring
        for line in lines:
            print(f"{Fore.CYAN}{Style.BRIGHT}{line}{Style.RESET_ALL}")

    elif style == "azure":
        # Pixelated style with precise TDX letters
        lines = [
            "┌─────────────────────────────────────┐",
            "│                                     │",
            "│   ████████  ██████   ██    ██      │",
            "│      ██     ██   ██   ██  ██       │",
            "│      ██     ██   ██    ████        │",
            "│      ██     ██   ██     ██         │",
            "│      ██     ██████     ████        │",
            "│                                     │",
            "│         TDX Python CLI              │",
            "└─────────────────────────────────────┘",
        ]

        # Print with blue to cyan gradient
        colors = [
            Fore.BLUE,
            Fore.BLUE,
            Fore.CYAN,
            Fore.CYAN,
            Fore.LIGHTBLUE_EX,
            Fore.LIGHTBLUE_EX,
            Fore.LIGHTCYAN_EX,
            Fore.LIGHTCYAN_EX,
            Fore.WHITE,
            Fore.BLUE,
        ]

        for i, line in enumerate(lines):
            color = colors[min(i, len(colors) - 1)]
            print(f"{color}{Style.BRIGHT}{line}{Style.RESET_ALL}")

    else:  # default style
        lines = [
            "  ______  ____   _  __   ____          __  __                 _____ __    ____",
            " /_  __/ / __ \\ / |/ /  / __ \\ __  __ / /_/ /_  ____  ____   / ___// /   /  _/",
            "  / /   / / / //    /  / /_/ // / / // __/ __ \\/ __ \\/ __ \\  \\__ \\/ /    / /  ",
            " / /   / /_/ // /|  / / ____// /_/ // /_/ / / / /_/ / / / / ___/ / /____/ /   ",
            "/_/    \\____//_/ |_/ /_/     \\__, / \\__/_/ /_/\\____/_/ /_/ /____/_____/___/   ",
            "                            /____/                                            ",
        ]
        # Print with cyan to blue gradient
        colors = [
            Fore.CYAN,
            Fore.CYAN,
            Fore.BLUE,
            Fore.BLUE,
            Fore.LIGHTBLUE_EX,
            Fore.LIGHTBLUE_EX,
        ]
        for i, line in enumerate(lines):
            color = colors[min(i, len(colors) - 1)]
            print(f"{color}{Style.BRIGHT}{line}{Style.RESET_ALL}")

    print()


# Display the bordered TDX Python CLI ASCII art
def display_bordered_ascii():
    """Display the bordered TDX Python CLI ASCII text art"""
    lines = [
        " _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _ ",
        "|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|",
        "|_|                                                                                                            |_|",
        "|_|                                                                                                            |_|",
        "|_|  .___________. _______  ___   ___    .______   ____    ____ .___________. __    __    ______   .__   __.   |_|",
        "|_|  |           ||       \\ \\  \\ /  /    |   _  \\  \\   \\  /   / |           ||  |  |  |  /  __  \\  |  \\ |  |   |_|",
        "|_|  `---|  |----`|  .--.  | \\  V  /     |  |_)  |  \\   \\/   /  `---|  |----`|  |__|  | |  |  |  | |   \\|  |   |_|",
        "|_|      |  |     |  |  |  |  >   <      |   ___/    \\_    _/       |  |     |   __   | |  |  |  | |  . `  |   |_|",
        "|_|      |  |     |  '--'  | /  .  \\     |  |          |  |         |  |     |  |  |  | |  `--'  | |  |\\   |   |_|",
        "|_|      |__|     |_______/ /__/ \\__\\    | _|          |__|         |__|     |__|  |__|  \\______/  |__| \\__|   |_|",
        "|_|                                                                                                            |_|",
        "|_| _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _ |_|",
        "|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|",
    ]

    # Create a gradient from cyan to blue for the border
    # and white for the text inside
    for i, line in enumerate(lines):
        if i <= 2 or i >= 10:  # Border lines (top and bottom)
            print(f"{Fore.CYAN}{Style.BRIGHT}{line}{Style.RESET_ALL}")
        else:  # Text lines
            # Split the line into border and content
            if len(line) > 4:  # Make sure the line is long enough to split
                border_left = line[:4]  # Get "|_|  "
                content = line[4:-4]  # Get the middle content
                border_right = line[-4:]  # Get "  |_|"

                # Print with colors
                print(
                    f"{Fore.CYAN}{Style.BRIGHT}{border_left}{Fore.WHITE}{content}{Fore.CYAN}{border_right}{Style.RESET_ALL}"
                )
            else:
                print(f"{Fore.CYAN}{Style.BRIGHT}{line}{Style.RESET_ALL}")

    print()


# Also add a pixelated style that more closely matches the image
def display_pixelated_tdx():
    """Display a pixelated TDX logo similar to the image shared"""
    lines = [
        "┌────────────────────────────────┐",
        "│                                │",
        "│  ████████ ████████ ██      ██ │",
        "│     ██       ██     ██    ██  │",
        "│     ██       ██      ██  ██   │",
        "│     ██       ██       ████    │",
        "│     ██       ██       ██ ██   │",
        "│     ██       ██      ██  ██   │",
        "│     ██       ██     ██    ██  │",
        "│                                │",
        "│        TDX Python CLI          │",
        "└────────────────────────────────┘",
    ]

    # Create a nice gradient from teal to blue
    colors = [
        Fore.BLUE,
        Fore.BLUE,
        Fore.CYAN,
        Fore.LIGHTCYAN_EX,
        Fore.LIGHTCYAN_EX,
        Fore.LIGHTBLUE_EX,
        Fore.LIGHTBLUE_EX,
        Fore.BLUE,
        Fore.BLUE,
        Fore.BLUE,
        Fore.WHITE,
        Fore.BLUE,
    ]

    for i, line in enumerate(lines):
        color = colors[min(i, len(colors) - 1)]
        print(f"{color}{Style.BRIGHT}{line}{Style.RESET_ALL}")

    print()


# Box drawing utilities
def box(content, width=60, style="single"):
    """Create a box around content text

    Args:
        content (str): Text to place in the box
        width (int): Width of the box
        style (str): Box style ('single', 'double', 'rounded')

    Returns:
        str: Formatted box with content
    """
    chars = {
        "single": {"tl": "┌", "tr": "┐", "bl": "└", "br": "┘", "h": "─", "v": "│"},
        "double": {"tl": "╔", "tr": "╗", "bl": "╚", "br": "╝", "h": "═", "v": "║"},
        "rounded": {"tl": "╭", "tr": "╮", "bl": "╰", "br": "╯", "h": "─", "v": "│"},
    }

    box_style = chars.get(style, chars["single"])

    # Calculate padding
    padding = width - 2  # Account for the vertical borders

    # Create the box
    result = []
    result.append(f"{box_style['tl']}{box_style['h'] * padding}{box_style['tr']}")

    # Add content with word wrap
    words = content.split()
    line = ""
    for word in words:
        if len(line) + len(word) + 1 <= padding - 2:  # -2 for the space on either side
            line += " " + word if line else word
        else:
            # Add the current line and start a new one
            spaces = padding - len(line) - 2
            result.append(f"{box_style['v']} {line}{' ' * spaces} {box_style['v']}")
            line = word

    # Add the last line
    if line:
        spaces = padding - len(line) - 2
        result.append(f"{box_style['v']} {line}{' ' * spaces} {box_style['v']}")

    # Add the bottom of the box
    result.append(f"{box_style['bl']}{box_style['h'] * padding}{box_style['br']}")

    return "\n".join(result)


# Color and decoration utilities
def header(text):
    """Format text as a header"""
    return f"{Fore.CYAN}{Style.BRIGHT}{text}{Style.RESET_ALL}"


def subheader(text):
    """Format text as a subheader"""
    return f"{Fore.MAGENTA}{Style.BRIGHT}{text}{Style.RESET_ALL}"


def info(text):
    """Format text as information"""
    return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"


def success(text):
    """Format text as success message"""
    return f"{Fore.GREEN}{text}{Style.RESET_ALL}"


def error(text):
    """Format text as error message"""
    return f"{Fore.RED}{text}{Style.RESET_ALL}"


def prompt(text):
    """Format text as a prompt"""
    return f"{Fore.GREEN}{text}{Style.RESET_ALL}"


def highlight(text):
    """Format text as highlighted information"""
    return f"{Fore.WHITE}{Style.BRIGHT}{text}{Style.RESET_ALL}"


def divider(char="-", length=40, color=Fore.CYAN):
    """Create a divider line with specified character, length and color"""
    return f"{color}{char * length}{Style.RESET_ALL}"


def format_person_summary(person):
    """Format a person's basic information for display

    Args:
        person (dict): Person data to format

    Returns:
        str: Formatted string with person info
    """
    if not person:
        return error("Unknown person")

    name = person.get("FullName", "Unknown")
    email = person.get("PrimaryEmail", "No email")
    uid = person.get("UID", "N/A")

    return f"{highlight(name)} ({info(email)}) - UID: {success(uid)}"


def display_person_details(person):
    """Display detailed information about a person

    Args:
        person (dict): Person data to display
    """
    if not person:
        print(error("No person details available."))
        return

    print(f"\n{subheader('Person Details:')}")
    print(divider())

    # Basic information
    print(f"{info('Name:')} {highlight(person.get('FullName', 'Unknown'))}")
    print(f"{info('Email:')} {person.get('PrimaryEmail', 'No email')}")
    print(f"{info('Username:')} {person.get('Username', 'N/A')}")
    print(f"{info('UID:')} {success(person.get('UID', 'N/A'))}")

    status_color = Fore.GREEN if person.get("IsActive") else Fore.RED
    status_text = "Active" if person.get("IsActive") else "Inactive"
    print(f"{info('Status:')} {status_color}{status_text}{Style.RESET_ALL}")

    # Additional details if available
    if person.get("Title"):
        print(f"{info('Title:')} {person['Title']}")
    if person.get("Phone"):
        print(f"{info('Phone:')} {person['Phone']}")
    if person.get("AlternatePhone"):
        print(f"{info('Alt Phone:')} {person['AlternatePhone']}")
    if person.get("MobilePhone"):
        print(f"{info('Mobile:')} {person['MobilePhone']}")
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
        print(f"{info('Address:')} {', '.join(address)}")

    # Show organizational details
    if person.get("OrganizationalID"):
        print(f"{info('Org ID:')} {person['OrganizationalID']}")
    if person.get("DefaultAccountID"):
        print(f"{info('Default Account ID:')} {person['DefaultAccountID']}")

    # Show custom attributes if available
    if person.get("Attributes") and len(person["Attributes"]) > 0:
        print(f"\n{subheader('Custom Attributes:')}")
        for attr in person["Attributes"]:
            print(f"  {info(attr.get('Name', 'Unknown'))}: {attr.get('Value', 'N/A')}")

    # Show groups if available
    if person.get("GroupIDs") and len(person["GroupIDs"]) > 0:
        print(f"\n{subheader('Groups:')}")
        for group_id in person["GroupIDs"]:
            print(f"  {success(group_id)}")

    # Show applications if available
    if person.get("Applications") and len(person["Applications"]) > 0:
        print(f"\n{subheader('Applications:')}")
        for app in person["Applications"]:
            # Handle both string values and object values
            if isinstance(app, dict):
                print(f"  {highlight(app.get('Name', 'Unknown'))}")
            else:
                print(f"  {highlight(app)}")


def display_people_list(people):
    """Display a list of people with option to select one

    Args:
        people (list): List of people to display

    Returns:
        str: The UID of the selected person, or None if no selection was made
    """
    if not people:
        print(error("No results found."))
        return None

    print(f"\n{info('Found')} {success(str(len(people)))} {info('people:')}")
    print(divider())

    for i, person in enumerate(people, 1):
        print(
            f"{Fore.WHITE}{i}. {highlight(person.get('FullName', 'Unknown'))} ({info(person.get('PrimaryEmail', 'No email'))})"
        )
        print(f"   {info('UID:')} {success(person.get('UID', 'N/A'))}")

        # Display additional information if available
        details = []
        if person.get("Title"):
            details.append(f"{info('Title:')} {person['Title']}")
        if person.get("Phone"):
            details.append(f"{info('Phone:')} {person['Phone']}")
        if person.get("IsActive") is not None:
            status_color = Fore.GREEN if person["IsActive"] else Fore.RED
            status_text = "Active" if person["IsActive"] else "Inactive"
            details.append(
                f"{info('Status:')} {status_color}{status_text}{Style.RESET_ALL}"
            )

        if details:
            print(f"   {' | '.join(details)}")

        print()

    # Prompt for selection
    print(
        f"\n{info('Enter a number to view person details, or press Enter to return to menu.')}"
    )
    selection = input(prompt(f"Select person [1-{len(people)}]: ")).strip()

    if selection and selection.isdigit():
        index = int(selection) - 1
        if 0 <= index < len(people):
            return people[index].get("UID")
        else:
            print(error("Invalid selection."))

    return None
