import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

webdriver_path = 'C:/chromedriver/chromedriver.exe'  

service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

def get_tide_data_for_month(year, month):
    url = f'https://surfguru.com.br/previsao/mare/60220/m?mes={month:02d}&ano={year}'
    
    driver.get(url)

    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'celula_dia'))
    )

    days = driver.find_elements(By.CLASS_NAME, 'celula_dia')

    month_data = []

    for day in days:
        day_data = day.text.strip()
        month_data.append(day_data)

    return month_data

year_data = {}

year = 25
for month in range(1, 13):
    print(f"Coletando dados para {month:02d}/{year}...")

    month_data = get_tide_data_for_month(year, month)
    
    year_data[f"{year}-{month:02d}"] = month_data

with open(f'tabua_mare_{year}.json', 'w', encoding='utf-8') as f:
    json.dump(year_data, f, ensure_ascii=False, indent=4)

driver.quit()

print(f"Dados de maré para o ano {year} foram exportados para 'tabua_mare_{year}.json'")
