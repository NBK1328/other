import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
#Использование маркеров тестов. Для использование заданных маркеров, создать файл pytest.ini
#pytest -s -v -m smoke name_file -прямой запуск тестов по ЗАДАННОМУ маркеру
#pytest -s -v -m "not smoke" name_file - инверсионный запуск тестов по ЗАДАННОМУ ИСКЛЮЧАЮЩЕМУ маркеру "not"
#pytest -s -v -m "smoke or regression" name_file - объединенный запуск тестов, по ЗАДАННЫМ маркерам "or"
#Смотреть test_fixture81.py для примера использования нескольких маркеров


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke # smoke test
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression #regression test
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
