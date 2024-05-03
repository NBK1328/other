from selenium import webdriver
import  time
from selenium.webdriver.common.by import By

try:
    driver = webdriver.Chrome()
    link = "https://suninjuly.github.io/execute_script.html"
    driver.get(link)
    button = driver.find_element(By.TAG_NAME, "button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button) #Скролл
    button.click()
    time.sleep(3)

finally:
    driver.quit()