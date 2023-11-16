from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time



def visma_løn_login_func(brugernavn_text, password_text, cvr_text):
    driver = webdriver.Chrome()
    driver.get("https://logon.bluegarden.dk/?applicationname=MLE-MSEUI")
    hold = WebDriverWait(driver, 10)
    long_hold = WebDriverWait(driver, 100)
    
    
    
    
 
    """ cvr_box = driver.find_element(By.ID, "cvr") """
    cvr_box = hold.until(EC.presence_of_element_located((By.ID, "cvr")))
    """ brugernavn_box = driver.find_element(By.ID, "userName") """
    brugernavn_box = hold.until(EC.presence_of_element_located((By.ID, "userName")))   
    """ password_box = driver.find_element(By.ID, "password") """
    password_box = hold.until(EC.presence_of_element_located((By.ID, "password")))
    """ sumbit_button = driver.find_element(By.ID, "btnNext") """
    sumbit_button = hold.until(EC.presence_of_element_located((By.ID, "btnNext")))
    
    print(brugernavn_text, password_text, cvr_text)
    
    cvr_box.send_keys("48117716")

    brugernavn_box.send_keys(brugernavn_text)

    password_box.send_keys(password_text)

    """ email_btn = driver.find_element(By.ID, "email") """
    email_btn = hold.until(EC.presence_of_element_located((By.ID, "email")))
    email_btn.click()

    sumbit_button.click()
    
    print("login done")

   
    time.sleep(1)
    """ input_element = driver.find_element(By.NAME, "filterField") """
    input_element = long_hold.until(EC.presence_of_element_located((By.NAME, "filterField")))
    input_element.send_keys(cvr_text)

    """ ok_button = driver.find_element(By.ID, "OK") """
    ok_button = long_hold.until(EC.presence_of_element_located((By.NAME, "OK")))
    ok_button.click()

    
    """ rapport1_btn = driver.find_element(By.ID, "sd41") """
    
    rapport_menu = hold.until(EC.element_to_be_clickable((By.ID, "sd41")))
    hover = ActionChains(driver).move_to_element(rapport_menu)
    hover.perform()
    rapport_menu.click()
    


    raport2_btn = long_hold.until(EC.element_to_be_clickable((By.ID, "sd42")))
    hover2 = ActionChains(driver).move_to_element(raport2_btn)
    hover2.perform()
    raport2_btn.click()

    iframe = hold.until(EC.presence_of_element_located((By.ID, "FContent")))
    driver.switch_to.frame(iframe)
    """ dropdown = driver.find_element(By.ID, "selectAktuelMenus") """
    dropdown = hold.until(EC.element_to_be_clickable((By.ID, "selectAktuelMenus")))
    select = Select(dropdown)
    select.select_by_visible_text("Afstemningsliste eIndkomst (år til dato)")
   
    continue_btn = hold.until(EC.presence_of_element_located((By.NAME, "ok")))
    continue_btn.click()


    def color_match(driver):
        download_btn = long_hold.until(EC.element_to_be_clickable((By.NAME, "download")))
        color = download_btn.value_of_css_property("background-color")
        return color == 'rgb(49, 99, 132)'
    download_btn = long_hold.until(EC.element_to_be_clickable((By.NAME, "download")))
    """ hover3 = ActionChains(driver).move_to_element(download_btn)
    hover3.perform """
   
    hold.until(color_match)
    download_btn.click

    print("done")
    
    
    driver.quit()