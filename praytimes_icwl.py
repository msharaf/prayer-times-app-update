import json
import csv
from google.oauth2 import service_account
import requests
import pygsheets
import datetime
import calendar
from hijri_converter import Hijri, Gregorian

### Get Current Date
now = datetime.datetime.now()
year = now.year
month = now.month

days_in_month = calendar.monthrange(year, month)[1]
# print(days_in_month)

current_month_number = datetime.datetime.now().month
current_month_name = datetime.datetime.strftime(datetime.datetime.strptime(str(current_month_number), '%m'), '%B')

client = pygsheets.authorize(service_account_file='prayertimes-update-sheet-387956f811cc.json')

# client = pygsheets.authorize(service_account_file='prayertimes-update-sheet-612221be5646.json')
sheet = client.open_by_key('16y5WU9MkXMjPKUYW1lIz26cIB-pkIznF-_qSOMpsUak')
wks = sheet.worksheet_by_title('Sheet3')
# print(wks)

# print(wks.get_as_df().to_json()) 
num_of_rows= wks.rows

# row = wks.get_row(2, include_tailing_empty=False)

wks1 = sheet.worksheet_by_title('Sheet1')

# index = 10
# wks1.update_row(index, row, col_offset=0)
# print(num_of_rows)
for x in range(1,num_of_rows+1):
    row = wks.get_row(x)
    # print(row[0],row[1])
    for y in range(1,days_in_month+1):
        # print(y)
        if(row[0]== str(month) and row[1] == str(y) ):
            hijri_date = Gregorian(year, month, y).to_hijri()
            # print(hijri_date)
            hijri_date_tuple = date_tuple=hijri_date.datetuple()
            if( hijri_date.day_name()) == "Friday":
               date_values=[row[1],row[2],row[8],row[3],row[4],'13:00',row[5],row[10],row[6],row[11],row[7],row[12],hijri_date.month_name(),hijri_date_tuple[2],hijri_date_tuple[0],current_month_name,year,hijri_date.day_name()]
            else:   
                date_values=[row[1],row[2],row[8],row[3],row[4],row[9],row[5],row[10],row[6],row[11],row[7],row[12],hijri_date.month_name(),hijri_date_tuple[2],hijri_date_tuple[0],current_month_name,year,hijri_date.day_name()]
            wks1.update_row(y, date_values)
