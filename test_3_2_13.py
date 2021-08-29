from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        welcome_text=browser.find_element_by_xpath("/html/body/div/h1")

        input1 = browser.find_element_by_xpath("//*[contains(text(), 'First name*')]/../input[@class='form-control first']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//*[contains(text(), 'Last name*')]/../input[@class='form-control second']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//*[contains(text(), 'Email*')]/../input[@class='form-control third']")
        input3.send_keys("@mail")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(10)

        browser.quit()

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        welcome_text=browser.find_element_by_xpath("/html/body/div/h1")

        input1 = browser.find_element_by_xpath("//*[contains(text(), 'First name*')]/../input[@class='form-control first']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//*[contains(text(), 'Last name*')]/../input[@class='form-control second']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//*[contains(text(), 'Email*')]/../input[@class='form-control third']")
        input3.send_keys("@mail")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        
        time.sleep(1)

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(10)

        browser.quit()

if __name__ == "__main__":
    unittest.main(exit=False)