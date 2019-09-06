from selenium import webdriver
import time

try: 
	
	from selenium import webdriver

	browser = webdriver.Chrome()
	browser.implicitly_wait(5)
	browser.get("http://suninjuly.github.io/wait1.html")
	button = browser.find_element_by_id("verify")
	button.click()
	message = browser.find_element_by_id("verify_message")
	
	assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()