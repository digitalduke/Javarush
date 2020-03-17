import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
	browser = webdriver.Chrome()
	yield browser
	browser.quit()

@pytest.mark.parametrize('page_code', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_guest_should_see_login_link(browser, page_code):
	link = "https://stepik.org/lesson/%d/step/1" % page_code
	browser.get(link)

	text_area = WebDriverWait(browser, 10).until(
		EC.visibility_of_element_located((By.CSS_SELECTOR, ".textarea"))
	)
	answer = math.log(int(time.time()))
	text_area.send_keys(str(answer))

	submit_button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
	submit_button.click()

	pre_tag = WebDriverWait(browser, 10).until(
		EC.visibility_of_element_located((By.TAG_NAME, "pre"))
	)

	assert pre_tag.text == "Correct!"
