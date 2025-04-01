import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"
#В PyTest есть стандартные метки, которые позволяют пропустить тест при сборе тестов для запуска (то есть не запускать тест) или запустить, 
#но отметить особенным статусом тот тест, который ожидаемо упадёт из-за наличия бага, чтобы он не влиял на результаты прогона всех тестов. 
#Эти метки не требуют дополнительного объявления в pytest.ini.
#Чтобы пропустить тест, его отмечают в коде как @pytest.mark.skip
#pytest -s -v name_file - для запуска без маркеров, не требуется аргумент -m. Если есть любой маркер, не использовать маркер пропуска теста
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# Если маркировка skip добавляется к функции, где уже есть другие маркировки, то skip должен быть последним маркером, иначе пропускаться не будет. 
# @pytest.mark.regression
# @pytest.mark.win10
# @pytest.mark.skip 