import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.ozon.ru/")

try:
    #find = driver.find_element(By.CSS_SELECTOR, "[placeholder='Искать на Ozon']")
    #find.send_keys("Обувница")
    #driver.find_element(By.CSS_SELECTOR, "[class='ag01-a']").click()


    time.sleep(5)

finally:
    driver.quit()
