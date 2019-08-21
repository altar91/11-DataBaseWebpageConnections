import requests
import json
import warnings
from requests_ntlm import HttpNtlmAuth
warnings.filterwarnings("ignore")
from bs4 import BeautifulSoup as Soup


user_credentials = {
    'username': 'user_name',
    'password': 'password',
    'domain': 'domain'
}

# Creating a class for Authentication


class UserAuthentication:

    def __init__(self, username, password, domain, site_url):
        self.__username = username
        self.__password = password
        self.__domain = domain
        self.__site_url = site_url
        self.__ntlm_auth = None

    def authenticate(self):
        login_user = self.__domain + "\\" + self.__username  # username example: winntdomain/dibyaranjan
        user_auth = HttpNtlmAuth(login_user, self.__password)
        self.__ntlm_auth = user_auth

        my_headers = {
            'accept': 'application/json;odata=verbose',
            'content-type': 'application/json;odata=verbose',
            'odata': 'verbose',
            'X-RequestForceAuthentication': 'true'
        }

        result = requests.get(self.__site_url, auth=user_auth, headers=my_headers, verify=False)
        if result.status_code == requests.codes.ok:
            return result
        else:
            result.raise_for_status()

if __name__ == '__main__':
    conn = psycopg2.connect(**params)
    username = user_credentials['username']
    password = user_credentials['password']
    domain = user_credentials['domain']
    site_url = "SharePoint_list_url"
    auth_object = UserAuthentication(username, password, domain, site_url)
    result = auth_object.authenticate()
    soup = Soup(result.text, "lxml-xml")
