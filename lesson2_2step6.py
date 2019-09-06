from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
	
	from selenium import webdriver

	browser = webdriver.Chrome()
	link = "http://SunInJuly.github.io/execute_script.html"
	browser.get(link)
	
	x_element = browser.find_element_by_id("input_value")
	x = x_element.text
	y = calc(x)
	# Ваш код, который заполняет обязательные поля
	browser.find_element_by_id("answer").send_keys(y)
	
	option1 = browser.find_element_by_css_selector('[type="checkbox"]')
	option1.click()
	
	option2 = browser.find_element_by_id("robotsRule")
	browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
	option2.click()
	
	button = browser.find_element_by_tag_name("button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	#browser.execute_script("window.scrollBy(0, 100);")
	button.click()
	assert True

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()