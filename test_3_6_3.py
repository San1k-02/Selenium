import time
import math
import pytest
import unittest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
#@pytest.mark.parametrize('number', ["236895"])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(6)
        
    answer = str(math.log(int(time.time() +0.2))) 
    answer_box=browser.find_element_by_xpath('/html/body/div[1]/div[2]/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[2]/div/div/div/textarea')
    answer_box.send_keys(answer)

    time.sleep(1)

    button=browser.find_element_by_xpath('/html/body/div[1]/div[2]/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[4]/button')
    button.click()

    time.sleep(1)

    assert browser.find_element_by_xpath("/html/body/div[1]/div[2]/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/div/div[1]/div[2]/div/pre").text=="Correct!"

    time.sleep(1)

    browser.quit()
# import pytest
# from selenium import webdriver

# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# def test_guest_should_see_login_link(browser, language):
#     link = f"http://selenium1py.pythonanywhere.com/{language}/"
#     browser.get(link)
#     browser.find_element_by_css_selector("#login_link")