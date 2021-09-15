# Description of the project

This projet aims to build a website that scrape the US treasury daily financial data from the website [1], and to plot them to logged users. 

The emploied stack is the following: 
Frontend : ReactJS
Backend : Flask
Users DB : SQLite 
Financial data DB : InfluxDB


The python code (backend) is divided in two blueprints: 
  - auth: which manage user registration authentication. The user registration is submitted via a confimation process: an email with a link is sent to the user. If you want to test the user registration you can use a temporary email (reference [2]).
  - main. which manage the data scraping, the DB loading (and uploading) and the REST API to send to the frontend the graphs

The ReactJS code (frontend) presents de following pages : Register, Login, Confirmation account and show_data.

The project also provide an easy set up of all the dependecies thanks to the docker-compose.yml file. 

# Run the project

To run the code follow the following steps:

Replace the "xxx.xxx.xxx.xxx" string with the local IP in line 6 of the file: backend\flaskr\main\db_config.py 

Then, run the following commands: 

docker-compose up -d

pip install bs4 influxdb_client requests
python .\backend\flaskr\main\scrape_hist_data.py -> to download the data in the folder DATA
python .\backend\flaskr\main\db_loading.py -> to load the time series DB

then you can run the site at http://localhost:3000/ and test all the functionalities.


References : 
[1] https://fsapps.fiscal.treasury.gov/dts/issues/collapsed
[2] https://temp-mail.org/en/



