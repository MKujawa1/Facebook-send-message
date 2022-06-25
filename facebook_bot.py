from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def conf():
    '''
    Set the chrome configuration. Get driver with start URL

    Returns
    -------
    driver : WebDriver object
        Driver with configuration and messanger URL.

    '''
    ### Facebook messanger URL
    URL = 'https://www.facebook.com/messages'
    ### Set CHROME options
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    ### Init driver
    driver = webdriver.Chrome('chromedriver.exe',chrome_options=chrome_options)
    driver.get(URL)
    return driver

def login(driver,email,password):
    '''
    Login to facebook.

    Parameters
    ----------
    driver : WebDriver object
        Driver from conf.
    email : str
        Your email to facebook account.
    password : str
        Your password to facebook account.

    Returns
    -------
    driver : WebDriver object
        Driver to send_message.

    '''
    ### Wait for element to be clickable and click allow for cookies
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]'))).click()
    ### Send email and password
    driver.find_element(By.ID, 'email').send_keys(email)
    driver.find_element(By.ID, 'pass').send_keys(password)
    ### Click login button
    driver.find_element(By.ID,'loginbutton').click()
    return driver

def send_message(driver, person, message):
    '''
    Send message to person

    Parameters
    ----------
    driver : WebDriver object
        Driver from login.
    person : list
        Person to send message.
    message : list
        Message to send.

    '''
    ### Search for person
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/div/label/input'))).send_keys(person)
    ### Click on person
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a'))).click()
    ### Sleep to avoid error
    time.sleep(1)
    ### Send message
    wait = WebDriverWait(driver, 20)
    send = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[1]')))
    send.send_keys(message)
    send.send_keys(Keys.RETURN)