import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

from datetime import date, timedelta
from time import sleep

selenium_path = "C:\\Users\\Enrique M\\OneDrive\\Documentos\\Marco\\Web Development\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=selenium_path)

date_ = date.today()

web_data = f"https://www.wunderground.com/hourly/mx/silao/date/{date_ + timedelta(days=1)}"
driver.get(url=web_data)
sleep(5)
cloud_cover_sheet = pd.DataFrame({"Hora": ["24:00", "1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00", "8:00",
                                           "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00",
                                           "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]})
title_days = [date_+timedelta(days=2), date_ + timedelta(days=3), date_ + timedelta(days=4), date_ + timedelta(days=5),
              date_ + timedelta(days=6), date_ + timedelta(days=7), date_ + timedelta(days=8)]

for day in range(7):
    cloud_cover_data = []
    for hour in range(1, 25):
        cloud_cover = driver.find_element(By.XPATH, f'//*[@id="hourly-forecast-table"]/tbody/tr[{hour}]/td[7]/lib-display-unit/span/span[1]').text
        cloud_cover_data.append(cloud_cover+"%")
    cloud_cover_sheet[title_days[day]] = cloud_cover_data
    next_day = driver.find_element(By.XPATH, '//*[@id="nextDay"]/button')
    next_day.click()
    sleep(2)
driver.quit()
cloud_cover_sheet.to_csv(f"{date_}CloudCover.csv")
print("El archivo con las predicciones se ha creado exitosamente.")
