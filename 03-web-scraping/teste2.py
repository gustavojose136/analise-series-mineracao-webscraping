from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

webdriver_path = 'C:/chromedriver/chromedriver.exe'

service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

url = 'https://surfguru.com.br/previsao/mare/60220/m?mes=05&ano=25'

driver.get(url)

data = {}
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'celula_dia'))
    )

    days = driver.find_elements(By.CLASS_NAME, 'celula_dia')

    for day in days:
        try:
            day_text = day.find_element(By.CLASS_NAME, 'linha_data_lua').text.strip()
        except Exception as e:
            print(f"Erro ao tentar encontrar o dia: {e}")
            continue

        day_number, day_name = day_text.split(" - ")
        tides = []

        mare_data = day.find_elements(By.CSS_SELECTOR, '.celula_mare, .celula_mare_baixa')
        for mare in mare_data:
            try:
                hour, height = mare.text.strip().split('h ')
                tides.append({
                    "hora": hour + "h",
                    "altura": height
                })
            except Exception as e:
                print(f"Erro ao tentar encontrar marés: {e}")
                continue
        try:
            sun_info = day.find_element(By.XPATH, ".//div[contains(text(), 'Nascer do Sol')]/following-sibling::div").text
            sun_rise, sun_set = sun_info.split(' - ')
        except:
            sun_rise, sun_set = "N/A", "N/A"

        try:
            moon_info = day.find_element(By.XPATH, ".//div[contains(text(), 'Nascer da Lua')]/following-sibling::div").text
            moon_rise, moon_set = moon_info.split(' - ')
        except:
            moon_rise, moon_set = "N/A", "N/A"

        data[day_number] = {
            "dia": day_name,
            "marés": tides,
            "sol": {
                "nasce": sun_rise,
                "se_põe": sun_set
            },
            "lua": {
                "nasce": moon_rise,
                "se_põe": moon_set
            }
        }

    data["marés"] = {
        "alta": {
            "altura": "1.9",
            "dias": ["08", "09", "10"]
        },
        "baixa": {
            "altura": "-0.3",
            "dia": "07"
        }
    }

finally:
    driver.quit()

with open("previsao_mare.json", "w", encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Dados exportados com sucesso!")
