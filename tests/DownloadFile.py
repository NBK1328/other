import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/file_input.html")
dir = os.path.abspath((os.path.dirname("DownloadFile")))  #указываем директорию исполняемого файла
filePath = os.path.join(dir, 'NewFile.txt')  #Берем нужный файл, находящийся в директории dir

try:
    driver.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys("123")
    driver.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys("123")
    driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("123")
    driver.find_element(By.ID, "file").send_keys(filePath)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


    time.sleep(5)

finally:
    driver.quit()

