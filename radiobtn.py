import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    driver.get("https://suninjuly.github.io/math.html")

    xElement = driver.find_element(By.ID, "input_value")
    x = xElement.text
    formula = str(math.log(abs(12*math.sin(int(x)))))

    btn = driver.find_element(By.CLASS_NAME, "form-control")
    btn.send_keys(formula)

    driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
    driver.find_element(By.ID, "robotsRule").click()
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()

    time.sleep(5)
finally:

    driver.quit()