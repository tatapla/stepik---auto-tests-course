import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

answer = str(math.log(int(time.time())))
print(answer)

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('num', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_send_response(browser, num):
	link = f"https://stepik.org/lesson/{num}/step/1"
	browser.get(link)
	browser.implicitly_wait(15)
	browser.find_element_by_tag_name("textarea").send_keys(str(math.log(int(time.time()))))
	browser.find_element_by_css_selector(".submit-submission ").click()
	message = browser.find_element_by_css_selector(".smart-hints__hint")
	
	assert "Correct!" == message.text
	