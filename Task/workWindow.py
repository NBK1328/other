import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/alert_accept.html")

try:
    driver.find_element(By. CSS_SELECTOR, "[type='submit']").click()
    alert = driver.switch_to.alert
    alert.accept()
    num = driver.find_element(By.ID, "input_value")
    numTxt = int(num.text)
    formula = str(math.log(abs(12*math.sin(numTxt))))
    driver.find_element(By.CSS_SELECTOR,
                        "[class='form-control']").send_keys(formula)
    driver.find_element(By.CSS_SELECTOR,
                        "button[type='submit']").click()







    time.sleep(5)

finally:
    driver.quit()
