import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    driver = webdriver.Chrome()
    driver.get("https://suninjuly.github.io/selects1.html")

    sumNum = sum([int(driver.find_element(By.ID, "num1").text),
                  int(driver.find_element(By.ID, "num2").text)])

    select = Select(driver.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sumNum))

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


    time.sleep(3)


finally:
    driver.quit()
