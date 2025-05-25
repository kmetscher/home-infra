import requests
from os import environ

IPIFY_URL = 'https://api.ipify.org'
GODADDY_API_URL = 'https://api.godaddy.com/v1/'
API_KEY = environ.get('GODADDY_API_KEY')
API_SECRET = environ.get('GODADDY_API_SECRET')
DOMAIN = 'cringe.solutions'

def get_current_ip() -> str:
    return requests.get(IPIFY_URL).text

def get_record_ip() -> str:
    headers = {'Authorization': f"sso-key {API_KEY}:{API_SECRET}"}
    return requests.get(f"{GODADDY_API_URL}domains", headers=headers).text

def main():
    print(get_record_ip())

if __name__ == '__main__':
    main()
