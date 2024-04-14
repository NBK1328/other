import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    driver = webdriver.Chrome()
    driver.get("https://suninjuly.github.io/get_attribute.html")
    valSunduk = driver.find_element(By.CSS_SELECTOR, "img[src='images/chest.png'")
    valueX = valSunduk.get_attribute("valuex")
    formula = str(math.log(abs(12*math.sin(int(valueX)))))
    driver.find_element(By.ID, "answer").send_keys(formula)
    driver.find_element(By.ID, "robotCheckbox").click()
    driver.find_element(By.ID, "robotsRule").click()
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(5)
finally:

    driver.quit()