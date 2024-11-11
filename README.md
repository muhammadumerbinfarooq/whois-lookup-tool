# WHOIS Lookup Tool

A simple Python tool to fetch and display WHOIS information for domain names.

## Features

- Fetches WHOIS information for any domain name.
- Displays registrar, creation date, expiration date, and name servers.
- Easy to use and extend.

## Requirements

- Python 3.x
- `python-whois` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/muhammadumermemon/whois-lookup-tool.git
    cd whois-lookup-tool
    ```

2. Install the required library:
    ```bash
    pip install python-whois
    ```

## Usage

1. Run the script:
    ```bash
    python whois_lookup.py
    ```

2. Enter the domain name when prompted.

## Example

```bash
Enter the domain name: example.com
Domain Name: example.com
Registrar: Example Registrar, Inc.
Creation Date: 1995-08-13 04:00:00
Expiration Date: 2025-08-12 04:00:00
Name Servers: ns1.example.com, ns2.example.com
