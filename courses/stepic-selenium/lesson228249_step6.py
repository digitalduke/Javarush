from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_value = browser.find_element(By.ID, "input_value")
answer = calc(x_value.text)

answer_input = browser.find_element(By.ID, "answer")
answer_input.send_keys(answer)

checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

browser.execute_script("window.scrollBy(0, 100);")

radiobutton = browser.find_element(By.ID, "robotsRule")
radiobutton.click()

browser.execute_script("window.scrollBy(0, 100);")

submit = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
submit.click()
