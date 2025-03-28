import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

#scope - Область видимости для использование фикстуры. Работают для  “function”, “class”, “module”, “session”.
#Откроется один экземпяр браузера для одного комплекта тестов. Так же, в этом примере используется yield для финализатора кода ИЗ ЗА ОБЛАСТИ ВИДИМОСТИ SCOPE.
#Есть альтернативный способ вызова teardown кода с помощью встроенной фикстуры request и ее метода addfinalizer
#После завершения теста, который вызывал фикстуру, выполнение фикстуры продолжится со строки, следующей за строкой со словом yield
#Так же, реализованно не классически, а с использованием "Возвращаемого значения" 
#По умолчанию фикстура будет создаваться для каждого тестового метода, то есть для каждого теста запустится свой экземпляр браузера
@pytest.fixture(scope='class') 
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")