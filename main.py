from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dash
from dash import html

service = Service(executable_path="/usr/local/bin/chromedriver")
url = 'https://www.bankbazaar.com/fixed-deposit-rate.html'

driver = webdriver.Chrome(service=service)
driver.get(url)

data = driver.find_elements(By.XPATH, "//div[contains(@class,'hfm-table')][1]//tr")

headings = []
fixed_rates_data = []

for i in range(len(data)):
    bank_name = driver.find_element(By.XPATH,
                                    "//div[contains(@class, 'hfm-table')][1]//tr[" + str(i + 1) + "]//td[1]").text
    rate_general = driver.find_element(By.XPATH,
                                       "//div[contains(@class, 'hfm-table')][1]//tr[" + str(i + 1) + "]//td[2]").text
    rate_senior = driver.find_element(By.XPATH,
                                      "//div[contains(@class, 'hfm-table')][1]//tr[" + str(i + 1) + "]//td[3]").text
    x = {
        'Bank Name': bank_name,
        'General Citizen Rate': rate_general,
        'Senior Citizen Rate': rate_senior
    }
    fixed_rates_data.append(x)

del fixed_rates_data[0]

bank_names = []
citizen_rates = []
scitizen_rates = []

for data in fixed_rates_data:
    bank_names.append(data['Bank Name'])
    citizen_rates.append(data['General Citizen Rate'])
    scitizen_rates.append(data['Senior Citizen Rate'])


df = pd.DataFrame(fixed_rates_data)

barWidth = 0.25

br1 = np.arange(len(citizen_rates))
br2 = [x + barWidth for x in br1]

plt.bar(br1, citizen_rates, color='b', width=barWidth, edgecolor='grey', label='General Citizen Rate')
plt.bar(br2, scitizen_rates, color='g', width=barWidth, edgecolor='grey', label='Senior Citizen Rate')

plt.xlabel('Bank Name', fontweight='bold', fontsize=15)
plt.ylabel('TD Rate', fontweight='bold', fontsize=15)
plt.xticks([r + barWidth for r in range(len(citizen_rates))], bank_names, rotation='vertical')

# print(df)
# plt.show()

# Dashboard

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("PLease Work")
])

if __name__ == '__main__':
    app.run_server(debug=True)
