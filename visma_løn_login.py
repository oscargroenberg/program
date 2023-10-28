from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



def visma_løn_login_func(brugernavn_text, password_text, cvr_text):
    driver = webdriver.Chrome()
    
    driver.get("https://logon.bluegarden.dk/?applicationname=MLE-MSEUI")
    time.sleep(2)
    cvr_box = driver.find_element(By.ID, "cvr")
    brugernavn_box = driver.find_element(By.ID, "userName")
    password_box = driver.find_element(By.ID, "password")
    sumbit_button = driver.find_element(By.ID, "btnNext")
    
    
    
    time.sleep(1)
    cvr_box.send_keys("48117716")
    brugernavn_box.send_keys(brugernavn_text)
    password_box.send_keys(password_text)
    time.sleep(10)
    sumbit_button.click()
    time.sleep(30)
    print("login done")
    ok_button = driver.find_element(By.ID, "OK")
    input_element = driver.find_element(By.NAME, "filterField")
    input_element.send_keys(cvr_text)
    ok_button.click()
    time.sleep(1)
    rapport1_btn = driver.find_element(By.ID, "sd41")
    raport2_btn = driver.find_element(By.ID, "sd42")
    rapport1_btn.click()
    time.sleep(0.5)
    raport2_btn.click()



    time.sleep(10)

    
    time.sleep(10)
    driver.quit()