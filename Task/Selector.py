import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# brow = webdriver.Chrome()
# brow.get("https://suninjuly.github.io/simple_form_find_task.html")

def form(brow):
    a = brow.find_element(By.NAME, "first_name")
    a.send_keys("Lol")
    b = brow.find_element(By. NAME, "last_name")
    b.send_keys("kek")
    c = brow.find_element (By. CLASS_NAME, "city")
    c.send_keys("chebyrek")
    d = brow.find_element(By.ID, "country")
    d.send_keys("pistolet")
    button = brow.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

# brow = webdriver.Chrome()
# brow.get("https://suninjuly.github.io/simple_form_find_task.html")
# form()
#
# time.sleep(20)
# brow.quit()