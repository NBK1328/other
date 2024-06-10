import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try:
    driver = webdriver.Chrome()
    driver.get("https://suninjuly.github.io/selects1.html")
    def ex1():
        # driver = webdriver.Chrome()
        # driver.get("https://suninjuly.github.io/selects1.html")

        driver.find_element(By. TAG_NAME, "select")
        driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
        driver.find_element(By.CSS_SELECTOR, "[value='1']").click()

    def ex2(): #Метод библиотеки специально под select т.е выбор
        select = Select(driver.find_element(By.TAG_NAME, "select"))
        select.select_by_value("1")
        #  select.select_by_visible_text("text") - по тексту
        #  select.select_by_index(index) - по индексу списка

    ex2()
    time.sleep(3)

finally:

    driver.quit()
