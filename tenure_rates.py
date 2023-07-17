import dash
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
import socket
from comp_interest_rate_plot import fig_1 as tenure_plot
from comp_interest_rate_plot import fig as indiv_plot
from historical_plot import fig as historic_plot

web_service = Service('/usr/local/bin/chromedriver.exe')
url = 'https://www.paisabazaar.com/fixed-deposit/'

options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dve-shm-uage')

driver = webdriver.Chrome(service=web_service, options=options)
driver.get(url)

small_bank_rates = []
private_bank_rates = []

for i in range(12):
    bank_name = driver.find_element(By.XPATH,
                                    "//div[contains(@class, 'wpb_text_column')][2]//tr[" + str(i + 3) + "]//td[1]").text
    highest = driver.find_element(By.XPATH,
                                  "//div[contains(@class, 'wpb_text_column')][2]//tr[" + str(i + 3) + "]//td[2]").text
    year_1 = driver.find_element(By.XPATH,
                                 "//div[contains(@class, 'wpb_text_column')][2]//tr[" + str(i + 3) + "]//td[3]").text
    year_3 = driver.find_element(By.XPATH,
                                 "//div[contains(@class, 'wpb_text_column')][2]//tr[" + str(i + 3) + "]//td[4]").text
    year_5 = driver.find_element(By.XPATH,
                                 "//div[contains(@class, 'wpb_text_column')][2]//tr[" + str(i + 3) + "]//td[5]").text
    item = {
        'Bank Name': bank_name,
        'Highest Slab': highest,
        '1 year Tenure': year_1,
        '3 year Tenure': year_3,
        '5 year Tenure': year_5
    }

    small_bank_rates.append(item)

for i in range(23):
    bank_name = driver.find_element(By.XPATH,
                                    "//div[contains(@class, 'wpb_text_column')][3]//table[1]//tr[" + str(
                                        i + 3) + "]//td[1]").text
    highest = driver.find_element(By.XPATH,
                                  "//div[contains(@class, 'wpb_text_column')][3]//table[1]//tr[" + str(
                                      i + 3) + "]//td[2]").text
    year_1 = driver.find_element(By.XPATH,
                                 "//div[contains(@class, 'wpb_text_column')][3]//table[1]//tr[" + str(
                                     i + 3) + "]//td[3]").text
    year_3 = driver.find_element(By.XPATH,
                                 "//div[contains(@class, 'wpb_text_column')][3]//table[1]//tr[" + str(
                                     i + 3) + "]//td[4]").text
    year_5 = driver.find_element(By.XPATH,
                                 "//div[contains(@class, 'wpb_text_column')][3]//table[1]//tr[" + str(
                                     i + 3) + "]//td[5]").text
    item = {
        'Bank Name': bank_name,
        'Highest Slab': highest,
        '1 year Tenure': year_1,
        '3 year Tenure': year_3,
        '5 year Tenure': year_5
    }

    private_bank_rates.append(item)

df_1 = pd.DataFrame(small_bank_rates)
df_2 = pd.DataFrame(private_bank_rates)

# tenure_plot.show()

# barWidth = 0.25
#
# citizen_rates = df_2['Highest Slab'].astype(float)
# bank_names = df_2['Bank Name']
#
# br1 = np.arange(len(citizen_rates))
# br2 = [x + barWidth for x in br1]
#
# plt.bar(br1, citizen_rates, color='b', width=barWidth, edgecolor='grey', label='General Citizen Rate')
#
# plt.ylim(7, 8.50)
#
# plt.xlabel('Bank Name', fontweight='bold', fontsize=15)
# plt.ylabel('Highest Slab', fontweight='bold', fontsize=15)
# plt.xticks([r + barWidth for r in range(len(citizen_rates))], bank_names, rotation='vertical')
#
# plt.show()

# # Attempting to plot bar graph with plotly
#
# dff = df_2.copy()
# dff = dff[['Bank Name', 'Highest Slab']]
# dff['Highest Slab'] = dff['Highest Slab'].astype(float)
#
# figure = px.bar(
#     data_frame=dff,
#     x='Bank Name',
#     y='Highest Slab',
# )
# figure.update_layout(yaxis_range=[6.90, 8.50])
#
# figure.show()
#
# # End

# PLOT

df_2['Highest Slab'] = df_2['Highest Slab'].astype(float)
fig = px.bar(df_2, x='Bank Name', y='Highest Slab')
fig.update_layout(yaxis=dict(range=[7.0, 8.10], dtick=0.1))
