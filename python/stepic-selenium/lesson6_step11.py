from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

first_name_field = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class .first")
first_name_field.send_keys("Ivan")
last_name_field = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class .second")
last_name_field.send_keys("Petrov")
email_field = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class .third")
email_field.send_keys("mail@mail.ru")

submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
submit_button.click()

time.sleep(1)

welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
welcome_text = welcome_text_elt.text

assert welcome_text == "Поздравляем! Вы успешно зарегистировались!"
