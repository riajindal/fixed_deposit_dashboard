import dash
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
import socket

web_service = Service('/usr/local/bin/chromedriver.exe')
url_kotak = 'https://www.paisabazaar.com/fixed-deposit/kotak-mahindra-bank-fd-rates/'
url_icici = 'https://www.paisabazaar.com/fixed-deposit/icici-bank-fd-rates/'

options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dve-shm-uage')

driver = webdriver.Chrome(service=web_service, options=options)
driver.get(url_icici)

kotak_tenure_rates = []
element_found = False
i = 0

while not element_found:
    try:
        tenure = driver.find_element(By.XPATH,
                                     "//div[contains(@class, 'wpb_text_column')][2]//tr[" + str(
                                         i + 3) + "]//td[1]").text
        general_rate = driver.find_element(By.XPATH,
                                           "//div[contains(@class, 'wpb_text_column')][2]//tr[" + str(
                                               i + 3) + "]//td[2]").text
        senior_rate = driver.find_element(By.XPATH,
                                          "//div[contains(@class, 'wpb_text_column')][2]//tr[" + str(
                                              i + 3) + "]//td[3]").text

        item = {
            'Tenure': tenure,
            'General Rate': general_rate,
            'Senior Rate': senior_rate,
        }

        kotak_tenure_rates.append(item)
        i += 1

    except NoSuchElementException:
        element_found = True
        break

df_1 = pd.DataFrame(kotak_tenure_rates)

pattern = r'\d+'
res = re.findall(pattern, df_1.iloc[0, 0])
df_1['Tenure'] = df_1['Tenure'].astype(str)


def format_tenure(value):
    value = value.replace("–", "-")
    value = value.replace("to", "-")
    p = r'\([^)]*\)'
    value = re.sub(p, '', value)

    return value


df_1['Tenure'] = df_1['Tenure'].apply(format_tenure)
df_1[['Min Value', 'Max Value']] = df_1['Tenure'].str.split('-', expand=True)


def convert_to_days(duration):
    days = 0
    if duration is None:
        return 0
    matches = re.findall(r'(\d+)\s*(days?|months?|years?)', duration, re.IGNORECASE)
    for match in matches:
        value, unit = match
        if unit.lower() in ['day', 'days']:
            days += int(value)
        elif unit.lower() in ['month', 'months']:
            days += int(value) * 30  # Assuming 30 days in a month
        elif unit.lower() in ['year', 'years']:
            days += int(value) * 365  # Assuming 365 days in a year

    return days


# df_1.to_csv('icici_slabs.csv', index=False, mode='w')