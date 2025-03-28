import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
#При описании фикстуры можно указать дополнительный параметр autouse=True, который укажет, 
# что фикстуру нужно запустить для каждого теста даже БЕЗ ЯВНОГО ВЫЗОВА

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome() 
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(autouse=True) #ИСПОЛЬЗУЕМЫЙ ПАРАМЕТР
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")