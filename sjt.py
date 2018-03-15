from time import sleep
from random import randint

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

def getRandomName():
	arrayNombres = ["Dr. Elver Galarga", "Unfe Tomás", "Richard Dawkins", "Luis Lopez", "Juan Manuel de Rosas", "Mauricio Macri", "Bill Gates"]
	return arrayNombres[randint(0, len(arrayNombres)-1)]

def main():
	for i in range(0, 100):
		driver.get("http://www.comunidadsanjudastadeo.org/contacto.php")
		print("Entrando a SJT.")

		name = getRandomName()
		e = driver.find_element_by_xpath("//input[@id='nombre']")
		e.send_keys(name)
		
		e = driver.find_element_by_xpath("//input[@id='email']")
		e.send_keys(name.replace(" ", "").lower() + "@gmail.com")

		e = driver.find_element_by_xpath("//textarea[@id='mensaje']")
		e.send_keys("Su sistema ha sido comprometido.")

		e = driver.find_element_by_xpath("//input[@id='button']")
		e.send_keys(Keys.RETURN)

		sleep(15)
main()

#Cierra el navegador
#driver.close()
