from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
	
	from selenium import webdriver

	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser.get(link)

	# Ваш код, который заполняет обязательные поля
	button = browser.find_element_by_tag_name("button")
	time.sleep(1)
	button.click()
	
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)

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