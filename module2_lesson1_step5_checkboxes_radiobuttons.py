from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    input_element = browser.find_element_by_css_selector("#answer")
    input_element.send_keys(y)
    checkbox_element = browser.find_element_by_css_selector(".form-check-label[for = 'robotCheckbox']")
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
