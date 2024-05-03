import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/huge_form.html")
    elements = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
    for element in elements:
        element.send_keys("123")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(10)
    print(len(elements))
    driver.quit()

