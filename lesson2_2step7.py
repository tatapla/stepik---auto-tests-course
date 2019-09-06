from selenium import webdriver
import time
import os

try: 
	
	from selenium import webdriver

	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/file_input.html"
	browser.get(link)

	# Ваш код, который заполняет обязательные поля
	browser.find_element_by_name("firstname").send_keys("FirstName")
	browser.find_element_by_name("lastname").send_keys("SecondName")
	browser.find_element_by_name("email").send_keys("email@email.ru")

	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
	element = browser.find_element_by_css_selector('[type="file"]')
	element.send_keys(file_path)
	
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