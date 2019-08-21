import requests
import io
import pandas
import getpass
from simple_salesforce import Salesforce

if __name__ == '__main__':
    try:
        sfconn = Salesforce(username="user_name", password="password.", security_token="security_token")


        data = requests.session().get("https://URL.salesforce.com/Report_Name?export=1&enc=UTF-8&xf=csv", headers=sfconn.headers, cookies={'sid': sfconn.session_id})
        df = pandas.read_csv(io.StringIO(data.text))

    finally:
        if conn is not None:
            conn.close()
