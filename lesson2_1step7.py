from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)

	img = browser.find_element_by_tag_name("img")
	x_element = img.get_attribute("valuex")
	y = calc(x_element)
    # Ваш код, который заполняет обязательные поля
	browser.find_element_by_id("answer").send_keys(y)
	
	option1 = browser.find_element_by_css_selector('[type="checkbox"]')
	option1.click()
	option1 = browser.find_element_by_id("robotsRule")
	option1.click()
    # Отправляем заполненную форму
	button = browser.find_element_by_css_selector('[type="submit"]')
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()