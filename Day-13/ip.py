import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "Could not resolve domain."

# Example usage
domain_name = input("Enter a domain name: ")
ip_address = get_ip_address(domain_name)

print(f"The IP address of {domain_name} is: {ip_address}")
