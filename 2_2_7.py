from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("/html/body/div/form/div/input[1]")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("/html/body/div/form/div/input[2]")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("/html/body/div/form/div/input[3]")
    input3.send_keys("@mail")

    element = browser.find_element_by_css_selector("[type='file']")
    element.send_keys("C://file.txt")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
