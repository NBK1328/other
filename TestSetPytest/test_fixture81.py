import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
#Смотреть файл test_fixture81.py, здесь же дополнение для использование НЕСКОЛЬКИХ маркеров.
<<<<<<< HEAD
#Маркеры smoke и win10
=======
#Маркеры smoke И win10
>>>>>>> 92f3b503de2650276f69757503d2162c67535fb8
#pytest -s -v -m "smoke and win10" file_name - запуск тестов с несколькими маркерами "and"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")