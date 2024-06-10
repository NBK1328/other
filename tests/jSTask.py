import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/execute_script.html")

try:
    num = driver.find_element(By.ID, "input_value")
    numTxt = int(num.text)
    formula = math.log(abs(12*math.sin(numTxt)))
    form = driver.find_element(By.CSS_SELECTOR, "[class='form-control'")
    form.send_keys(formula)
    driver.execute_script("return arguments[0].scrollIntoView(true);",num)  # Скролл
    driver.find_element(By.ID, "robotCheckbox").click()
    driver.find_element(By.ID, "robotsRule").click()
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    time.sleep(3)
finally:
    driver.quit()
