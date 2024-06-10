import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    brow = webdriver.Chrome()
    brow.get("https://suninjuly.github.io/find_link_text")
    link = brow.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

    a = brow.find_element(By.NAME, "first_name")
    a.send_keys("Lol")
    b = brow.find_element(By. NAME, "last_name")
    b.send_keys("kek")
    c = brow.find_element (By. CLASS_NAME, "city")
    c.send_keys("chebyrek")
    d = brow.find_element(By.ID, "country")
    d.send_keys("pistolet")
    button = brow.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(10)

finally:
    brow.quit()