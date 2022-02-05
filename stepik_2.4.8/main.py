import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    WebDriverWait(browser, 14).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'price')
    browser.find_element(By.ID, 'book').click()

    x = int(browser.find_element(By.ID, 'input_value').text)
    result = str(math.log(abs(12 * math.sin(x))))

    browser.find_element(By.ID, 'answer').send_keys(result)
    browser.find_element(By.ID, 'solve').click()
finally:
    time.sleep(10)
    browser.quit()
