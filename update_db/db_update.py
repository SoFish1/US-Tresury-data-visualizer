from typing import Text
from bs4 import BeautifulSoup
import requests, re
from db_loading import extract_points, extract_date
from db_config import write_api,bucket
from datetime import datetime



with open('/app/last_link.txt', 'r') as f:
    last_link= f.read()
    f.close()



#Get the last document DTS from the HTML page
class Daily_Tresaury_Statement:
    def __init__(self,text,date):
        self.text=text
        self.date=date
 
def download_last_DTS():

    main_url = "https://fsapps.fiscal.treasury.gov/dts/issues"
    req = requests.get(main_url)
    soup = BeautifulSoup(req.text, "html.parser")
    links = soup.find_all(href = re.compile("/dts/files/"), string=re.compile("TEXT"))
    sub_last_link = str(links[0]).replace('<a href="','').replace('" target="blank">TEXT</a>','')
    
    global last_link

    if  last_link != sub_last_link:
        last_link = "https://fsapps.fiscal.treasury.gov/" + sub_last_link
        req = requests.get(last_link)

        with open('/app/last_link.txt', 'w') as f:
            f.write(last_link)
            f.close()

        last_link=sub_last_link
        date=extract_date(last_link.replace("/dts/files/",""))
        DTS=Daily_Tresaury_Statement(text=req.text,date=date)


        return DTS
    else:
        return


def db_update():
    now = datetime.now()
    print("Influx DB updated at:", now.strftime("%d/%m/%Y %H:%M:%S"))

    DTS=download_last_DTS()
    if isinstance(DTS, Daily_Tresaury_Statement):
        points=extract_points(DTS.text.split("\n"),DTS.date)
        #try:
        write_api.write(bucket=bucket, record=points.deposits)
        write_api.write(bucket=bucket, record=points.withdrawal)

        #except AttributeError as e: 
        #    print ("The db is alreay updated")

if __name__=="__main__":
    db_update()

