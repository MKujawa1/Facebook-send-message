from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

URL = 'https://www.facebook.com/messages'
email = 'maciej.skate@gmail.com'
password = 'Db17603168'
person = 'Maciej Kujawa'
message = 'ok'

driver = webdriver.Chrome('chromedriver.exe',chrome_options=chrome_options)

driver.get(URL)

wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]'))).click()
driver.find_element(By.ID, 'email').send_keys(email)
driver.find_element(By.ID, 'pass').send_keys(password)
driver.find_element(By.ID,'loginbutton').click()

wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/div/label/input'))).send_keys(person)
wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a'))).click()
time.sleep(1)
wait = WebDriverWait(driver, 20)
send = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[1]')))
send.send_keys(message)
send.send_keys(Keys.RETURN)
