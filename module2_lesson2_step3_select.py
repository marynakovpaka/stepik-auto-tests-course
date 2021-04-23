from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(a,b):
    return (a + b)
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a = int(browser.find_element_by_css_selector("span[id = 'num1']").text)
    b = int(browser.find_element_by_css_selector("span[id = 'num2']").text)
    sum_numbers = str (calc(a, b))
    #metod1
    browser.find_element_by("select").click()
    browser.find_element_by_css_selector(f"[value = '{sum_numbers}']").click()
    #metod2
    # select = Select(browser.find_element_by_tag_name("select"))
    # select.select_by_visible_text(sum_numbers)

    browser.find_element_by_css_selector("button[type = 'submit']").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()