from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

#Тест работоспособности фикстуры browser в файле conftest. Описание настройки конфигурации теста в файле conftest.py

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
