import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    driver.get("https://suninjuly.github.io/find_xpath_form")
    a = driver.find_element(By.NAME, "first_name")
    a.send_keys("Lol")
    b = driver.find_element(By. NAME, "last_name")
    b.send_keys("kek")
    c = driver.find_element (By. CLASS_NAME, "city")
    c.send_keys("chebyrek")
    d = driver.find_element(By.ID, "country")
    d.send_keys("pistolet")
    button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
finally:
    time.sleep(10)
    driver.quit()