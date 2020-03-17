import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button = browser.find_element(By.ID, "book")
button.click()

x_value = browser.find_element(By.ID, "input_value")
answer = calc(x_value.text)

answer_input = browser.find_element(By.ID, "answer")
answer_input.send_keys(answer)

submit = browser.find_element(By.ID, "solve")
submit.click()
