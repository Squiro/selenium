import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

def main():
	driver.get("http://www.youtube.com")
	print("Entrando a YouTube.")

	e = driver.find_element_by_xpath("//input[@id='search']")
	
	e.send_keys("Los Gumer Enojado")
	e.send_keys(Keys.RETURN)

	driver.save_screenshot('screenie.png')

main()

#driver.close()
