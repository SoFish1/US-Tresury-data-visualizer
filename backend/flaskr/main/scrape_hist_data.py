from bs4 import BeautifulSoup
import requests, re, time
from os import chdir, getcwd 
#Identification of the DATA folder
local_path=getcwd()
chdir("DATA")
data_path=(getcwd())
print(data_path)

#main_url = "https://fsapps.fiscal.treasury.gov/dts/issues/collapsed"
#req = requests.get(main_url)
#soup = BeautifulSoup(req.text, "html.parser")

# Finding the main title tag.
years = [i for i in range(2021,2022)]



for j in range(0,len(years)): 
    
    sub_url="https://fsapps.fiscal.treasury.gov/dts/issues/" + str(years[j]) + "/1?sortOrder=desc#FY" + str(years[j])
    for i in range(1,5):
        
        sub_sub_url=sub_url+ "Q" + str(i)
        sub_sub_url= sub_sub_url.replace("/1?", "/" + str(i) + "?")

        req = requests.get(sub_sub_url)
        soup = BeautifulSoup(req.text, "html.parser")
        for ref in soup.find_all(href = re.compile("/dts/files/"), string=re.compile("TEXT")):
            sub_sub_url_daily=str(ref.attrs).replace("{'target': 'blank', 'href': '",'').replace("'}",'')
            req = requests.get("https://fsapps.fiscal.treasury.gov/" + sub_sub_url_daily)
            filename=sub_sub_url_daily.replace("/dts/files/",'')
            try:
                with open(data_path +"/" + filename, 'w', encoding='utf-8') as f:
                    print(str(req.text), file=f)
                f.close()
            except FileNotFoundError as e:
                print(e)    
            time.sleep(0.05)
    
   




