from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#setting the Edge driver
driver = webdriver.Edge()

#loading up website
driver.get("https://www.alibaba.com")
time.sleep(4)

#locating sign up button on home page
signin_button = driver.find_element("id","a2700.product_home_l0.home_header.i5.6b7667af7KbaEM")
signin_button.click()
time.sleep(4)

#signing into customer account
username_bar = driver.find_element("id","a2700.login.0.i0.56be1afaWMreeL")
username_bar.send_keys("sannitomi@outlook.com")
password_bar = driver.find_element("name","password")
password_bar.send_keys("maybelater24")
login_button=driver.find_element("id","a2700.login.0.i3.56be1afaspOapR")
login_button.click()
time.sleep(4)

#search for item
search_bar= driver.find_element("class","search-bar-input util-ellipsis")
search_bar.send_keys("humidifier")
search_bar.send_keys(Keys.RETURN)
time.sleep(4)

