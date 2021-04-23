from selenium import webdriver
import time
import math




def calc(x):
    return math.log(abs(12 * math.sin(x)))

browser = webdriver.Chrome()
try:
   link = "http://SunInJuly.github.io/execute_script.html"
   browser.get(link)
   x = int(browser.find_element_by_id("input_value").text)
   print(x)
   result = str(calc(x))
   print (result)
   browser.find_element_by_css_selector("input[id='answer']").send_keys(result)
   button = browser.find_element_by_tag_name("button")
   browser.execute_script("return arguments[0].scrollIntoView(true);", button)
   button.click()
   browser.find_element_by_css_selector(".form-check-label[for = 'robotCheckbox']").click()
   browser.find_element_by_css_selector(".form-check.form-radio-custom input[class='form-check-input']").click()
   browser.find_element_by_tag_name("button").click()




finally:
    time.sleep(10)
    browser.quit()
