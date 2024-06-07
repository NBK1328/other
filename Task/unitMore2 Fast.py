import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def FindElement(link):
    with webdriver.Chrome() as brow:

        brow.get(link)
        fir = brow.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input").send_keys("123")
        sec = brow.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input").send_keys("123")
        thir = brow.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input").send_keys("123")
        btn = brow.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(1)

        txt = brow.find_element(By.TAG_NAME, "h1")
        txt_txt = txt.text
        brow.quit()

        return txt_txt

class TestStep(unittest.TestCase):

    def test_step1(self):
        self.assertEqual(FindElement("https://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "step1 pzdc")


    def test_step2(self):
        self.assertEqual(FindElement("https://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "step2 pzdc")


if __name__ == "__main__":
    unittest.main()