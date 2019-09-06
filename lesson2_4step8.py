from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
	
	from selenium.webdriver.common.by import By
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
	from selenium import webdriver
	
	browser = webdriver.Chrome()
	
	browser.get("http://suninjuly.github.io/explicit_wait2.html")
	
	# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
	WebDriverWait(browser, 12).until(
			EC.text_to_be_present_in_element((By.ID, "price"), "$100")
		)
	button = browser.find_element_by_id("book")
	button.click()
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	browser.find_element_by_id("answer").send_keys(y)
	# Отправляем заполненную форму
	button = browser.find_element_by_css_selector('[type="submit"]')
	button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()