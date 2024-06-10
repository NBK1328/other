import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# СМОТРЕТЬ ФАЙЛ pytestExample там все исправленно

def FindElement(link):
    with webdriver.Chrome() as brow:

        brow.get(link)
        brow.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('knock')
        brow.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('knock')
        brow.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('Knock-knock')
        brow.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

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