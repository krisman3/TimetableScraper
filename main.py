import requests
from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

response = requests.get("www.superdoc.bg")

if response:
    pass
else:
    print("Website not reachable.")
