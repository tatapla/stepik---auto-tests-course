from selenium import webdriver
import time
import math

def calc(x, y):
  return str(int(x)+int(y))
  
try: 
	from selenium import webdriver

	browser = webdriver.Chrome()
	link = "https://SunInJuly.github.io/execute_script.html"
	browser.get(link)
	button = browser.find_element_by_tag_name("button")
	#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	browser.execute_script("window.scrollBy(0, 100);")
	button.click()
	assert True

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()