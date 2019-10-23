#Задание 2.4 Пример 2 из теории

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока не будет = 100
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

button1=browser.find_element_by_id("book")
button1.click()

# достаем х 

a=browser.find_element_by_id("input_value")
b=a.text
x=int(b)
y=log(abs(12*sin(x)))

input1 = browser.find_element_by_id("answer")
input1.send_keys(str(y))


button2 = browser.find_element_by_id("solve")
button2.click()



