from selenium import webdriver
import time
import math

def calc(x, y):
  return str(int(x)+int(y))
  
try: 
	link = "http://suninjuly.github.io/selects1.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element_by_id("num1")
	x = x_element.text
	y_element = browser.find_element_by_id("num2")
	y = y_element.text
	s = calc(x, y)
	print(s)
    # Ваш код, который заполняет обязательные поля
	from selenium.webdriver.support.ui import Select
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(s) # ищем элемент с текстом "Python
	#select.select_by_visible_text("text") и select.select_by_index(index)
    # Отправляем заполненную форму
	button = browser.find_element_by_css_selector('[type="submit"]')
	button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()