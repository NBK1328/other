import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

# XFail: помечать тест как ожидаемо падающий
# К маркировке xfail можно добавлять параметр reason. Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest -rx
# pytest -rx -v file_name - запуск теста с "rx" - reason
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail (reason="fixing this bug right now")  #Обозначение "ОЖИДАЕМО падающего теста" \ "reason" - вывод в консоль сообщения при "неожиданно успешном" результате
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")
