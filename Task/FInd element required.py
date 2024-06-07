from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/registration1.html"
    brow = webdriver.Chrome()
    brow.get(link)
    fir = brow.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input")
    fir.send_keys("123")
    sec = brow.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input")
    sec.send_keys("123")
    thir = brow.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input")
    thir.send_keys("123")

    btn = brow.find_element(By.CSS_SELECTOR, "button[type='submit']")
    btn.click()

    time.sleep(1)

    txt = brow.find_element(By.TAG_NAME, "h1")
    txt_txt = txt.text
    assert "Congratulations! You have successfully registered!" == txt_txt

finally:
    time.sleep(5)
    brow.quit()

