# TeamDynamix API CLI Tool

An interactive command-line interface for working with the TeamDynamix API.

## Features

- Authentication to TeamDynamix API (Production or Sandbox environments)
- People operations:
  - Search for people by name, email, etc.
  - Retrieve detailed person information by UID
  - Look up people by username
  - Get UIDs by username
- Ticket operations:
  - Search for tickets with various filters
  - View detailed ticket information
  - View ticket history and comments
  - Create new tickets
  - Add comments to existing tickets
- Easy to extend with new modules and functionality

## Project Structure

```
TeamDynamixAPIs/
├── teamdynamix/                # Main package
│   ├── __init__.py
│   ├── auth/                   # Authentication module
│   │   ├── __init__.py
│   │   └── client.py           # Authentication client
│   ├── people/                 # People operations module
│   │   ├── __init__.py
│   │   ├── client.py           # People API client
│   │   └── commands.py         # CLI commands for people operations
│   ├── tickets/                # Tickets operations module
│   │   ├── __init__.py
│   │   ├── client.py           # Tickets API client
│   │   └── commands.py         # CLI commands for ticket operations
│   └── utils/                  # Utility functions
│       ├── __init__.py
│       ├── cli.py              # General CLI utilities
│       └── tickets.py          # Ticket-specific utilities
├── teamdynamix_auth.py         # Base TeamDynamix authentication class
├── teamdynamix_cli.py          # Main CLI script
├── requirements.txt            # Dependencies
└── .env                        # Environment variables (not in repo)
```

## Setup

1. Clone the repository:

   ```
   git clone <repository-url>
   cd TeamDynamixAPIs
   ```

2. Install required packages:

   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your TeamDynamix credentials:

   ```
   # Copy the example file
   cp env.example .env

   # Edit .env with your credentials
   ```

## Usage

Run the CLI tool:

```
python teamdynamix_cli.py
```

The tool will prompt you to:

1. Select an environment (Sandbox or Production)
2. Authenticate to the TeamDynamix API
3. Display a menu of available operations

### People Operations

- Search for people by name, email, or other identifiers
- View detailed person information including custom attributes
- Look up people by username
- Get UIDs by username

### Ticket Operations

- Search for tickets with filters for title, status, requestor, etc.
- View detailed ticket information
- View ticket history and comments
- Create new tickets
- Add comments to existing tickets

## Extending the Tool

### Adding New API Operations

1. Create appropriate modules in the package structure:

   - Add a client class in the relevant module (e.g., `tickets/client.py`)
   - Add command functions in a commands file (e.g., `tickets/commands.py`)

2. Update the main CLI script to include the new functionality

### Adding New API Modules

1. Create a new directory under the `teamdynamix` package
2. Add `__init__.py`, `client.py`, and `commands.py` files
3. Implement the API client and CLI commands
4. Update the main script to include the new module

## Dependencies

- requests: HTTP library for API requests
- pyjwt: JSON Web Token implementation
- python-dotenv: Environment variable management
