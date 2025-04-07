import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import login


#link  = "https://stepik.org/lesson/236895/step/1"

class TestMain():
    
    @pytest.mark.parametrize("links", ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])      
    def test_loginin(self ,browser, links):
        
        
        link  = f"https://stepik.org/lesson/{links})/step/1"
        browser.get(link)
        browser.implicitly_wait(60)

        login = browser.find_element(By.CLASS_NAME, "navbar__auth_login")
        login.click()
        email = browser.find_element(By.ID, "id_login_email")
        email.send_keys(login.getLogin())
        password = browser.find_element(By.ID, "id_login_password")
        password.send_keys(login.GetPassword())
        browser.find_element(By.CLASS_NAME, "button_with-loader").click()
        
        time.sleep(5)
        
        browser.find_element(By.CLASS_NAME, "string-quiz__textarea").send_keys(str(math.log(int(time.time()))))
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        
        txt = browser.find_element(By.CLASS_NAME,"smart-hints__hint")
        txt1 = txt.text
        assert txt1 == "Correct!", "Failed, wrong answer"
        print(txt1)

        #correctAnswer = browser.find_element(By.XPATH, '//p[@class="smart-hints__hint" and contains(text(), "Incorrect code")]')
    