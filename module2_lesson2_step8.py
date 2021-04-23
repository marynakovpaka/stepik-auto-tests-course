from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    driver.find_element_by_css_selector("input[name = 'firstname']").send_keys("Marina")
    driver.find_element_by_css_selector("input[name = 'lastname']").send_keys("Kovpaka")
    driver.find_element_by_css_selector("input[name = 'email']").send_keys("kovpakamarina@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path =os.path.join(current_dir, 'file.txt')
    driver.find_element_by_id("file").send_keys(file_path)
    driver.find_element_by_css_selector("button[type = 'submit']").click()

finally:
    time.sleep(10)
    driver.quit()