from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
   
    browser.execute_script("window.scrollBy(0, 500);")

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer=browser.find_element_by_id("answer")
    answer.send_keys(y)

    sbutton = browser.find_element_by_xpath("//*[@id='solve']")
    sbutton.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
