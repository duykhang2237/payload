from urllib.parse import urlparse
import requests
import socket

url = "http://localhost:1337/flag"

def validate_url(url):
    valid_url = urlparse(url)
    if valid_url.hostname:
        try:
            ip_address = socket.gethostbyname(valid_url.hostname)
            if ip_address in ['127.0.0.1', '0.0.0.0'] or ip_address.startswith('192.168.'):
                print("Bad URL")
                return False
            else:
                return True
        except socket.gaierror:
            print("Invalid hostname:", valid_url.hostname)
            return False
    else:
        print("Invalid URL format")
        return False
if validate_url(url):
    response = requests.get(url)
