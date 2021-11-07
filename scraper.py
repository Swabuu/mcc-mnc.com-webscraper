import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

URL = 'https://www.mcc-mnc.com/'
TABLE = 'mncmccTable'

# Creating TS for unique file name
ts = str(int(time.time()))

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all('table',{'id':TABLE})

df = pd.read_html(str(table), converters={'MCC':str, 'MNC':str, 'Country Code':str})[0]

# Create JSON file
df.to_json('{}-mcc-mnc.json'.format(ts), orient='records')

# Create XLSX file
df.to_excel('{}mccmnc.xlsx'.format(ts), index = False)

# Create CSV file
df.to_csv('{}mccmnc.csv'.format(ts), index=False)
