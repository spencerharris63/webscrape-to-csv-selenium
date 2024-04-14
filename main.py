from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv

# PATH TO YOUR CHROMEDRIVER
service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

# FIND TABLE AND PRINT HEADER TO CHECK WE ARE IN CORRECT PLACE
driver.get("https://steamdb.info/")
table = driver.find_element(By.XPATH, "//*[@id='main']/div[2]/div[1]/div[1]/table")
# a_element = table.find_element(By.XPATH, ".//th/a[contains(text(), 'Most Played')]")
# print(a_element.text)

rows = table.find_elements(By.XPATH, ".//tbody/tr[contains(@class, 'app')]")

games_data = []

for row in rows[:15]:
    # Get all td elements in the row, skip the first one
    columns = row.find_elements(By.TAG_NAME, 'td')[1:]  # Skip the first column

    # Extract text from each of the remaining columns (game title, players now, 24 hour peak)
    game_title = columns[0].text
    players_now = columns[1].text
    hour_peak = columns[2].text

    # Append the data tuple to the list
    games_data.append((game_title, players_now, hour_peak))


driver.quit()

with open('most_played_games.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Game Title', 'Players Now', '24 Hour Peak'])  # Writing headers
    writer.writerows(games_data)  # Writing the data rows

print("Data written to most_played_games.csv successfully.")
