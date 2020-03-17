import os

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

first_name = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(2)")
first_name.send_keys("Vasya")

last_name = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(4)")
last_name.send_keys("Pupkin")

email = browser.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(6)")
email.send_keys("mail@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, __file__)

filename_button = browser.find_element(By.ID, "file")
filename_button.send_keys(file_path)

submit = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
submit.click()
