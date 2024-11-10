import whois

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return str(e)

def print_whois_info(whois_info):
    if isinstance(whois_info, str):
        print(whois_info)
    else:
        print(f"Domain Name: {whois_info.domain_name}")
        print(f"Registrar: {whois_info.registrar}")
        print(f"Creation Date: {whois_info.creation_date}")
        print(f"Expiration Date: {whois_info.expiration_date}")
        print(f"Name Servers: {whois_info.name_servers}")

if __name__ == "__main__":
    domain = input("Enter the domain name: ")
    whois_info = get_whois_info(domain)
    print_whois_info(whois_info)
