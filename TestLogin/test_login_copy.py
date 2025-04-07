import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import login


class TestMain():
    
    @classmethod
    def setup_class(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(30)
        self._login(self)
        
    @classmethod
    def teardown_class(self):
        self.browser.quit()
    
   
    def _login(self):
        self.browser.get("https://stepik.org/lesson/236895/step/1")        
        self.browser.find_element(By.CLASS_NAME, "navbar__auth_login").click()
        self.browser.find_element(By.ID, "id_login_email").send_keys(login.getLogin())
        self.browser.find_element(By.ID, "id_login_password").send_keys(login.getPassword())
        self.browser.find_element(By.CLASS_NAME, "button_with-loader").click()
        time.sleep(2)
    
    
    @pytest.mark.parametrize("links", ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
    def test_case1(self, links):

        
        
        link  = f"https://stepik.org/lesson/{links}/step/1"
        self.browser.get(link)            
        time.sleep(5)
        self.browser.find_element(By.CLASS_NAME, "string-quiz__textarea").send_keys(str(math.log(int(time.time()))))
        self.browser.find_element(By.CLASS_NAME, "submit-submission").click()
        
        txt = self.browser.find_element(By.CLASS_NAME,"smart-hints__hint")
        txt1 = txt.text
        assert txt1 == "Correct!", "Failed, wrong answer"
        print(txt1)

        

        #correctAnswer = browser.find_element(By.XPATH, '//p[@class="smart-hints__hint" and contains(text(), "Incorrect code")]')
    