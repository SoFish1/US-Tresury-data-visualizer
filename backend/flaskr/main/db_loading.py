from os import chdir, getcwd, listdir
from datetime import datetime
from re import compile, sub
from db_config import client,write_api,bucket


#Identification of the local DATA folder path
local_path=getcwd()
chdir("DATA")
data_path=(getcwd())

#Each point in a document is associated to a name and a value;
# These points are read in process_line() function.; 
class Raw_data_point():
    def __init__(self,name,value,y_value):
        self.name=name
        self.y_name="y_" + name
        self.value=value
        self.y_value=y_value

#The points extracted in a file are grouped in consistency with the;
# associated tag ex: (Deposit or Withdrawal), 
# This class is defined to assign to extracted_points the associated group  
class Extracted_points():
    def __init__(self,deposits,withdrawal):
        self.deposits=deposits
        self.withdrawal=withdrawal

#Extracting datetime object from filename
def extract_date(filename):   
    year=int(str(20)+filename[0]+filename[1])
    month=int(filename[2]+filename[3])
    day=int(filename[4]+filename[5])
    date = datetime(year, month, day, 12, 0, 0).isoformat()
    return date



#This function return the points in a file with the associated tag and date;
#The filename is given as argument Ex:("21060700.txt")
def process_file(filename):
    date = extract_date(filename)
    #print(d)
    chdir(data_path)

    f = open(filename, 'r')
    text_lines=f.readlines()
    f.close()

    return extract_points(text_lines,date)

#This function process the file text and return the points with the associated tag,
#A file line list is given as argument, as well as the date of the file
def extract_points(text_lines,date):
 
    deposit_fields={}
    withdrawal_fields={}


    #REGEX for Identification of the tables
    table_re_withdrawals=compile('\s+Withdrawals\s+Today')
    table_re_deposits=compile('\s+Deposits\s+Today')
    table_re_issues=compile('\s+Issues\s+Today')

    
    data_re = compile('\D+\s+\d+(\.\d+)?\D+\d+(\.\d+)?\D+\d+(\.\d+)?')
    tag=None


    for line in text_lines:
    
        if data_re.match(line) and tag is not None:
            if tag is "Deposits":
                point = process_line(line)
                deposit_fields[point.name]=point.value
                deposit_fields[point.y_name] = point.y_value
            elif tag is "Withdrawals":
                point = process_line(line)
                withdrawal_fields[point.name]=point.value             
                withdrawal_fields[point.y_name] = point.y_value
        if table_re_withdrawals.match(line):
            deposits_points=point_definition(deposit_fields,"Deposits",date)
                    
            tag="Withdrawals"

        if table_re_deposits.match(line):
            tag="Deposits"
    
        if table_re_issues.match(line):
            withdrawals_points=point_definition(withdrawal_fields,"Withdrawals",date) 
            break
    try:
        
        points=Extracted_points(deposits_points,withdrawals_points)
        return points
    except Exception as e:
        print(f"Extracted_points exception {e}")        

    


#This function receive as argument a line of the text which has been previously selected in;
#extract_points(). It allow to extract the field name and the value of each point
def process_line(line):
    
    line = sub('\d/', '', line)
    
    line=line.replace("$","")
    line=line.replace(",","")
    
    line=line.split()
    daily_data=line[-3]
    montly_data=line[-2]
    yearly_data=line[-1]
    name_data=" ".join(line[:-3])

    try:
        daily_data=int(daily_data)
    except ValueError:
        daily_data=0

    try:
        yearly_data=int(yearly_data)
    except ValueError:
        yearly_data=0


    result = Raw_data_point(name_data,daily_data,yearly_data)

    return result


#This function build the dictionnary structure which will be emploied;
# to perform the data upload to the database.
def point_definition(point_fields,tag,date):
    point={
        "measurement": "Treasury_data",
        "tags": {"tag": tag},
        "fields": point_fields,
        "time": date
    }
    return point




#Function to upload the scraped data to InfluxDB server 
def hist_data_loading():
    for filename in listdir(data_path):
        points=process_file(filename)

        
        try:
            write_api.write(bucket=bucket, record=points.deposits)
            write_api.write(bucket=bucket, record=points.withdrawal)

        except Exception as e: 
            print (e, filename)
    

if __name__ == "__main__":
    hist_data_loading()
    