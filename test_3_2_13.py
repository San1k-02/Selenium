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
    unittest.main()

#try: 
    #link = "http://suninjuly.github.io/registration2.html"
    #browser = webdriver.Chrome()
    #browser.get(link)

    # Ваш код, который заполняет обязательные поля
    #input1 = browser.find_element_by_xpath("//*[contains(text(), 'First name*')]/../input[@class='form-control first']")
    #input1.send_keys("Ivan")
    #input2 = browser.find_element_by_xpath("//*[contains(text(), 'Last name*')]/../input[@class='form-control second']")
    #input2.send_keys("Petrov")
    #input3 = browser.find_element_by_xpath("//*[contains(text(), 'Email*')]/../input[@class='form-control third']")
    #input3.send_keys("@mail")

    # Отправляем заполненную форму
    #button = browser.find_element_by_css_selector("button.btn")
    #button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    #time.sleep(1)

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

#finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    #time.sleep(10)
    # закрываем браузер после всех манипуляций
    #browser.quit()
