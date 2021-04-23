from selenium import webdriver
import math
import time

def funct (x):
    return str(math.log(abs(12*math.sin(x))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    img_element = browser.find_element_by_id("treasure")
    x_value = int(img_element.get_attribute("valuex"))
    answer = funct(x_value)
    input_element = browser.find_element_by_id("answer")
    input_element.send_keys(answer)
    checkbox_element = browser.find_element_by_id("robotCheckbox")
    checkbox_element.click()
    radiobutton_element = browser.find_element_by_css_selector("#robotsRule")
    radiobutton_element.click()
    submit_element = browser.find_element_by_css_selector("button[type='submit']")
    submit_element.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

