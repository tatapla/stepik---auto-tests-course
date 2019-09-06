from selenium import webdriver
import time
import math

def calc(x, y):
  return str(int(x)+int(y))
  
try: 
	from selenium import webdriver
	link = "http://suninjuly.github.io/selects1.html"
	browser = webdriver.Chrome()
	browser.get(link)

	#browser.execute_script("alert('Robots at work');")
	#Обратите внимание, что исполняемый JavaScript нужно заключать в кавычки (двойные или одинарные). Если внутри скрипта вам также понадобится использовать кавычки, а для выделения скрипта вы уже используете двойные кавычки, то в скрипте следует поставить одинарные:
	
	#browser.execute_script("document.title='Script executing';")
	#Такой формат записи тоже будет работать:
	
	#browser.execute_script('document.title="Script executing";')
	#Можно с помощью этого метода выполнить сразу несколько инструкций, перечислив их через точку с запятой. Изменим сначала заголовок страницы, а затем вызовем alert:
	
	browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()