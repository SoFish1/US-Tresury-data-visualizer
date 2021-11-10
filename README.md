# Description of the project
This project aims to run a website that scrapes the US treasury daily financial data from the [website](https://fsapps.fiscal.treasury.gov/dts/issues/collapsed), and to show them to logged users as time series plots.

The employed stack is the following: 
- Frontend : ReactJS 
- Backend: Flask 
- Users DB: SQLite 
- Financial data DB: InfluxDB

The python code (backend) is divided into two blueprints:

- auth: This blueprint manages user registration authentication. The user registration is submitted through a confirmation process: an email with a link is sent to the user. If you want to test the user registration you can use a [temporary email](https://temp-mail.org/en/).
- main: This blueprint manages the data scraping, the DB loading (and uploading), and the REST API to send the data to the frontend.
The ReactJS code (frontend) presents de following pages: Register, Login, Confirmation account, and show_data.

The project also provides an easy setup of all the dependencies thanks to the docker-compose.yml file.

# How to run the project
To run the code follow the following steps:

Replace the "xxx.xxx.xxx.xxx" string with the local IP in line 6 of the file: backend\flaskr\main\db_config.py

Then, run the following commands:

* docker-compose up -d
* pip install bs4 influxdb_client requests 
* python .\backend\flaskr\main\scrape_hist_data.py -> to download the data in the folder DATA 
* python .\backend\flaskr\main\db_loading.py -> to load the time series DB

Then you can run the site at http://localhost:3000/ and test all the functionalities.


# What to do next? 

The development phase of this project is ongoing, notably, I'd like to add the following features: 
- Backend automatic testing code
- A process to recover the lost passwords
- Daily update of the influxDB with cron
- A script to automatically run the website



