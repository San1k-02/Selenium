from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value1=browser.find_element_by_xpath("//*[@id='num1']")
    x = value1.text

    value2=browser.find_element_by_xpath("//*[@id='num2']")
    y = value2.text

    sum=str(int(x)+int(y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
