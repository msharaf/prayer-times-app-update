import pandas as pd
import json
import csv
from google.oauth2 import service_account
import requests
import pygsheets
import datetime
import calendar

### Get Current Date
now = datetime.datetime.now()
year = now.year
month = now.month

days_in_month = calendar.monthrange(year, month)[1]

#### get Hijri Dates for current month

url = "https://api.aladhan.com/v1/gToHCalendar/{month}/{year}"
hijri_dates = requests.get(url).json()
# print(hijri_dates)    
# print(hijri_dates['data'][0]['gregorian'])
# with open('prayertimes-update-sheet-387956f811cc.json') as source:
#     info = json.load(source)
# credentials = service_account.Credentials.from_service_account_info(info)

client = pygsheets.authorize(service_account_file='prayertimes-update-sheet-387956f811cc.json')


sheet = client.open_by_key('1wHhQfnG1oUn4OYldR-LDV_4zHHCd3_pXYgp3so5uwYw')

wks = sheet.worksheet_by_title('Sheet2')
# print(wks)

# print(wks.get_as_df().to_json()) 
num_of_rows= len(wks.get_as_df())

# row = wks.get_row(2, include_tailing_empty=False)

wks1 = sheet.worksheet_by_title('Sheet1')

# index = 10
# wks1.update_row(index, row, col_offset=0)

for x in range(1,num_of_rows):
    row = wks.get_row(x, include_tailing_empty=False)
    for y in range(1,days_in_month):
        if(row[0]== str(month) and row[1] == str(y) ):
            print(row)
            print(hijri_dates['data'][y]['gregorian'])
            date_values=[row[3]]
            wks1.update_row(y, date_values)


