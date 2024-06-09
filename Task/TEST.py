from selenium import webdriver
from selenium.webdriver.common.by import By
import time


br = webdriver.Chrome()
br.get("https://mail.ru/")
time.sleep(3)
br.quit()