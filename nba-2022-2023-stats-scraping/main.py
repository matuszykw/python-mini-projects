from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


driver = webdriver.Chrome('C:/Development/chromedriver.exe')
driver.get("https://www.nba.com/stats/teams/traditional?DateFrom=&DateTo=&PerMode=Totals&sort=PTS&dir=-1&Season=2022-23&SeasonType=Regular+Season")

col_names = []
stats_list = []

for i in range(2, 29):
    name = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/thead/tr/th[{i}]').text
    col_names.append(name)
 
for i in range(1, 31):
    temp_stats_list = []
    for j in range(2, 29):
        stat = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/tbody/tr[{i}]/td[{j}]').text
        temp_stats_list.append(stat)
    stats_list.append(temp_stats_list)

df = pd.DataFrame(stats_list, columns=col_names)
df.to_csv('out.csv')
 
# //*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/thead/tr/th[2]
# //*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/thead/tr/th[3]



# //*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/a/div/span
# //*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/tbody/tr[2]/td[2]/a/div/span
# //*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table/tbody/tr[1]/td[3]