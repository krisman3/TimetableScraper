import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

response = requests.get("https://superdoc.bg", verify=False)

if response:
    driver.get("https://superdoc.bg")
    specialty = Select(driver.find_element(By.ID, "specialty_id"))
    specialty.select_by_visible_text("Гастроентеролог")
    town = Select(driver.find_element(By.ID,"location"))
    town.select_by_visible_text("София град")
    driver.find_element(By.ID,"doc_name").send_keys("Спасова")
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.implicitly_wait(5)
    results = driver.find_element(By.ID, "search-results")
    print(results.text)

else:
    print("Website not reachable.")
