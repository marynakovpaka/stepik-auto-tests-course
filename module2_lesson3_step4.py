from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector("button[type = 'submit']").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = int(browser.find_element_by_css_selector("span[id = 'input_value']").text)
    browser.find_element_by_id("answer").send_keys(calc(x))
    browser.find_element_by_css_selector("button[type= 'submit']").click()
finally:
    time.sleep(10)
    browser.quit()
