from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector("button[type= 'submit']").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = int(browser.find_element_by_css_selector("span[id = 'input_value']").text)
    browser.find_element_by_id("answer").send_keys(calc(x))
    browser.find_element_by_css_selector("button[type='submit']").click()



finally:
    time.sleep(10)
    browser.quit()