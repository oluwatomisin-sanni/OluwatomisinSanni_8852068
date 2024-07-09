from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

#opening the site in chrome
driver.get("https://www.zappos.com/")
driver.maximize_window()
time.sleep(6)

#selecting the sandal category from the homepage
sandal= driver.find_element("xpath","//*[@id='main']/div/div/section[1]/div/article[3]/a")
sandal.click()
time.sleep(6)
assert "sandals" in driver.title
