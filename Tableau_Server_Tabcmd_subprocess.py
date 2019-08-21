import warnings
from requests_ntlm import HttpNtlmAuth
warnings.filterwarnings("ignore")
import subprocess

#Install tabcmd first

def DownloadFromTableauServer():
    year, wknumber=get_amazon_week(now)
    commands= (
        r'tabcmd login -s https://tableau.server_name.com/ -u user_name -p password',
        r'tabcmd get "views/tableauDashboardName/tableauDashboardViewName?" -f "D:/Users/user_name/Desktop/image_name.png',
        r'tabcmd export "tableauDashboardName/tableauDashboardViewName?" --pdf --pagesize unspecified --pagelayout landscape --width 1200 -f "D:/Users/user_name/Desktop/pdf_name.pdf',
        r'tabcmd logout'
        )
    for command in commands:
        subprocess.call(command, shell=True, cwd=r'C:/Program Files/Tableau/Tableau Server/2019.2/extras/Command Line Utility')

if __name__ == '__main__':
    try:
        DownloadFromTableauServer()
    except Exception as e:
        send_emailError()
