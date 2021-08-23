from selenium import webdriver
import time
import math
def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fbutton=browser.find_element_by_css_selector("button.btn")
    fbutton.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer=browser.find_element_by_id("answer")
    answer.send_keys(y)

    sbutton = browser.find_element_by_css_selector("button.btn")
    sbutton.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
