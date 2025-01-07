import whois
import logging
import threading
import socket
from queue import Queue
import json
import time
import hashlib

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Hashing function for securing domain data
def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Function to retrieve WHOIS information
def get_whois_info(domain, results_queue):
    try:
        w = whois.whois(domain)
        results_queue.put(w)
    except Exception as e:
        logging.error(f"Error retrieving WHOIS info for {domain}: {e}")
        results_queue.put(f"Error: {str(e)}")

# Function to print WHOIS information
def print_whois_info(whois_info):
    if isinstance(whois_info, str):
        print(whois_info)
    else:
        print(json.dumps({
            "Domain Name": whois_info.domain_name,
            "Registrar": whois_info.registrar,
            "Creation Date": whois_info.creation_date,
            "Expiration Date": whois_info.expiration_date,
            "Name Servers": whois_info.name_servers,
            "Data Hash": hash_data(whois_info.domain_name)
        }, indent=4))

# Multithreaded execution for handling multiple domains
def threaded_whois(domains):
    threads = []
    results_queue = Queue()

    for domain in domains:
        thread = threading.Thread(target=get_whois_info, args=(domain, results_queue))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    while not results_queue.empty():
        print_whois_info(results_queue.get())

if __name__ == "__main__":
    domains = input("Enter comma-separated domain names: ").split(",")
    threaded_whois(domains
