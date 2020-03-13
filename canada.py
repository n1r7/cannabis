import requests
import lxml.html as lh
import pandas as pd
from bs4 import BeautifulSoup as bs


# Define function that requests and returns content

def request_content(url=''):
    page = requests.get(url)
    doc = page.content
    return doc

# Canada licensing table
url = 'https://www.canada.ca/en/health-canada/services/drugs-medication/cannabis/industry-licensees-applicants/licensed-cultivators-processors-sellers.html'

# Scrape licensing table by passing url to request_content()
canada_licensing_table = request_content(url)

# Create BS object from licensing table
soup = bs(canada_licensing_table, 'lxml')

# Extract table
table = soup.find('table')
table_rows = table.find_all('tr')

# Column headers
col1 = table.find('th', {'id': 't1hc1'}).text
col2 = table.find('th', {'id': 't1hc2'}).text
col3 = table.find('th', {'id': 't1hc3'}).text
col4a = table.find('th', {'id': 't1hc4'}).text + str('  ') + table.find('th', {'id': 't1hc7'}).text
col4b = table.find('th', {'id': 't1hc4'}).text + str('  ') + table.find('th', {'id': 't1hc8'}).text
col5 = table.find('th', {'id': 't1hc5'}).text
col6 = table.find('th', {'id': 't1hc6'}).text

columns = [col1, col2, col3, col4a, col4b, col5, col6]

# Create dataframe
data = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.get_text(strip=True) for tr in td]
    data.append(row)

df = pd.DataFrame(data, columns=columns)
df.drop(index=[0,1], inplace=True)
df.reset_index(inplace=True)
df.drop(columns='index', inplace=True)

print(df)


# Save to CSV
df.to_csv('canada_licenses.csv')
