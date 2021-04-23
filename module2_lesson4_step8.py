from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc (x):
    return str (math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
  browser = webdriver.Chrome()
  browser.get(link)
  price = WebDriverWait(browser,15).until(EC.text_to_be_present_in_element((By.ID,'price'),"$100"))
  button_book = browser.find_element(By.ID,"book").click()
  x = int(browser.find_element(By.ID,"input_value").text)
  print(x)

  result = browser.find_element(By.ID,"answer").send_keys(calc(x))
  submit_button = browser.find_element(By.ID,'solve').click()





finally:
  time.sleep(10)
  browser.quit()
