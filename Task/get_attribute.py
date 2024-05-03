import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#Найти checked


try:
    driver = webdriver.Chrome()
    driver.get("https://suninjuly.github.io/math.html")
    people_radio = driver.find_element(By. ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked") # Сначал найти элемент, потом его артибут
    print(f"value of people radio: {people_checked} ") # Проверка и показ
    assert people_checked is not None, "People radio is not selected by default"
    robots_radio = (driver.find_element(By.ID, "robotsRule")
                    .get_attribute("checked"))
    robots_checked = robots_radio.get_attribute("checked")
    #assert robots_radio is not None, "ЛЕГЛО"
    btnSubmit = (driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
                 .get_attribute("disabled"))
    assert btnSubmit is not None, "ЛЕГЛО" # 10 секунд и не ляжет


    time.sleep(3)

finally:

    driver.quit()
