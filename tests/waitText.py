import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


try:
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    expTxt = "$100"
    WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    driver.find_element(By.ID, "book").click()

    num = driver.find_element(By.ID, "input_value")
    numTxt = int(num.text)
    formula = str(math.log(abs(12 * math.sin(numTxt))))
    driver.find_element(By.CSS_SELECTOR,
                        "[class='form-control']").send_keys(formula)
    driver.find_element(By.CSS_SELECTOR,
                        "button[type='submit']").click()

    alert = driver.switch_to.alert
    alertText = alert.text
    alert.accept()
    print(alertText)

    time.sleep(5)

finally:
    driver.quit()
