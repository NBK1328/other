import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Запустить один и тот же тест с разными входными параметрами. 
# Для этого используется декоратор @pytest.mark.parametrize()

# В @pytest.mark.parametrize() нужно передать параметр, который должен изменяться, и список значений параметра. 
# В самом тесте наш параметр тоже нужно передавать в качестве аргумента. 
# Обратите внимание, что внутри декоратора имя параметра оборачивается в кавычки, 
# а в списке аргументов теста кавычки не нужны.

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link (browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
    

# Можно задавать параметризацию также для всего тестового класса, 
# чтобы все тесты в классе запустились с заданными параметрами. 
# В таком случае отметка о параметризации должна быть перед объявлением класса: 

@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
