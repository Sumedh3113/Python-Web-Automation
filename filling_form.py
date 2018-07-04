from selenium import webdriver;
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

#webdriver driver = new ChromeDriver()
browser= webdriver.Chrome();
browser.get('http://url');#Enter url here

user_name = browser.find_element_by_id('q')
user_name.send_keys("pycon")

password = browser.find_element_by_id('q')
password.send_keys("pycon")

user_name.send_keys(Keys.RETURN)
password.send_keys(Keys.RETURN)

#time.sleep(3)
browser.close()