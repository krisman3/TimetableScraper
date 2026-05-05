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
    doc_name = Select(driver.find_element(By.ID,"doc_name"))
    doc_name.select_by_visible_text("Спасова")
    driver.find_element(By.CLASS_NAME, "btn btn-primary btn-lg align-self-start").click()
    driver.implicitly_wait(5)
    results = driver.find_elements(By.ID, "search-results-wrap")

else:
    print("Website not reachable.")
