from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
 
driver = webdriver.Firefox()

def main():
        email = "tu_email@aca.com"
        password = "tucontraseñaaca123"

        driver.get('https://www.facebook.com/')
        print("Entrando a Facebook")

        elem = driver.find_element_by_xpath("//input[@id='email']")
        elem.send_keys(email)

        elem = driver.find_element_by_xpath("//input[@id='pass']")
        elem.send_keys(password)
        
        elem.send_keys(Keys.RETURN)

        sleep(5)

        x = 0
        while x<1000:
                driver.get("https://www.facebook.com/sharer.php?u=youtube.com/losgumeroficial")
                postbutton = driver.find_element_by_xpath('//*[@id="u_0_1v"]')
                postbutton.click()
                print("Publicados:" , x)
                x = x+1
main()