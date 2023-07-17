from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import pandas as pd
import re

# WEB SCRAPING

# Web scraping prerequisites and configuration
web_service = Service('/usr/local/bin/chromedriver.exe')
url = 'https://sbi.co.in/web/interest-rates/interest-rates/base-rate-historical-data#show'

options = webdriver.ChromeOptions()
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dve-shm-uage')

driver = webdriver.Chrome(service=web_service, options=options)
driver.get(url)

# Scraping Tenure v/s Interest Rate Table
historical_data = []
element_found = False
i = 0

# result = driver.find_element(By.XPATH, "//div[contains(@class, 'table-responsive')]//table[contains(@class, 'table "
#                                        "table-bordered')]//tr[2]//td[1]").text
# print(result)
#
# for x in range(39):
#     effective_date = driver.find_element(By.XPATH, "//div[contains(@class, 'table-responsive')]//table[contains(@class, 'table table-bordered')]//tr["+str(x+2)+"]//td[1]").text
#     interest_rate = driver.find_element(By.XPATH, "//div[contains(@class, 'table-responsive')]//table[contains(@class, 'table table-bordered')]//tr["+str(x+2)+"]//td[2]").text
#
#
#     item = {
#         'Effective Date': effective_date,
#         'Interest Rate': interest_rate,
#     }
#
#     historical_data.append(item)
#
# print(historical_data)

while not element_found:
    try:
        effective_date = driver.find_element(By.XPATH,
                                             "//table[contains(@class, 'table table-bordered')]//tr[" + str(
                                                 i + 2) + "]//td[1]").text
        interest_rate = driver.find_element(By.XPATH,
                                            "//table[contains(@class, 'table table-bordered')]//tr[" + str(
                                                i + 2) + "]//td[2]").text

        item = {
            'Effective Date': effective_date,
            'Interest Rate': interest_rate,
        }

        historical_data.append(item)
        i += 1

    except NoSuchElementException:
        element_found = True
        break

# Storing table in a dataframe
df_1 = pd.DataFrame(historical_data)

# print(df_1)
df_1.to_csv('sbi_historical_data.csv', index=False, mode='w')
