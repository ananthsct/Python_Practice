from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from dotenv import load_dotenv
import os
import time
from getpass import getpass

load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options)
driver.get("https://www.google.com/")
time.sleep(3)
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='email']").send_keys('9673723765')
password = os.getenv("PASSWORD")
# password2 = getpass("Enter your password: ")
driver.find_element(By.XPATH, "//input[@id='pass']").send_keys(password)
time.sleep(2)
element = driver.find_element(By.XPATH, "//button[@name='login']")
WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, "//button[@name='login']")))
time.sleep(2)
element.click()
time.sleep(5)
search_box = driver.find_element(By.XPATH, "//input[@type='search']")
search_box.send_keys('Achutha Manickam', Keys.ENTER)
# search_box.send_keys(Keys.ENTER)
time.sleep(5)


input("Press Enter to close the browser...")   # this line will keep the browser open until the input given by user



