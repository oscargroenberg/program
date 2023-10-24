from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import time

def web_scrap(nemid_text):
    driver = webdriver.Chrome()

    keyboard = Controller()

    driver.get("https://pdcs.skat.dk/portallogin/digitalSignatur?userType=virksomhed&amp;targetUrl=aHR0cHM6Ly9udHNlLnNrYXQuZGsvbnRzZS1mcm9udC9mb3JzaWRl")


    time.sleep(5)
    
    
    keyboard.type(nemid_text)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    time.sleep(2)
    """ cookie_button.click() """
    time.sleep(2)
    """ login_button.click() """
    """ bruger_textbox.send_keys("CVR") """
    time.sleep(1)
    """ borger_button.click() """
    time.sleep(2)

    time.sleep(10)
    driver.quit()