import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

response = requests.get("https://superdoc.bg", verify=False)

if response:
    driver.get("https://superdoc.bg")
    specialty = Select(driver.find_element(By.NAME, "specialty_id"))
    specialty.select_by_visible_text("Гастроентеролог")
else:
    print("Website not reachable.")
