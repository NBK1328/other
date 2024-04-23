from selenium import webdriver
import  time
from selenium.webdriver.common.by import By

def jS ():
    try:
        driver = webdriver.Chrome()
        #driver.execute_script("alert('Robots at work');")
        #driver.execute_script("document.title='Script executing';")
        driver.execute_script("document.title='Script executing';alert('Robots at work');")

        time.sleep(3)


    finally:
        driver.quit()

def jS1 ():
    try:
        driver = webdriver.Chrome()
        link = "https://suninjuly.github.io/execute_script.html"
        driver.get(link)
        button = driver.find_element(By. TAG_NAME, "button").click()
        time.sleep(3)

    finally:
        driver.quit()
jS1()