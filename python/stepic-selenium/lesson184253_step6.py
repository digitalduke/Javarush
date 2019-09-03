from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

journey_button = browser.find_element(By.TAG_NAME, "button")
journey_button.click()

browser.switch_to.window(browser.window_handles[1])

x_value = browser.find_element(By.ID, "input_value")
answer = calc(x_value.text)

answer_input = browser.find_element(By.ID, "answer")
answer_input.send_keys(answer)

submit = browser.find_element(By.CSS_SELECTOR, "body > form > div > div > button")
submit.click()
