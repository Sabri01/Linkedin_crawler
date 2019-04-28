from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(insert path to chromedriver)
driver.get('http://linkedin.com')

username = driver.find_element_by_class_name('login-email')
username.send_keys('foo@gmail.com')

password = driver.find_element_by_id('login-password')
password.send_keys('bar')

sign_in = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in.click()
sleep(5)

driver.get('http://google.com')
search_query = driver.find_element_by_name('q')
search_query.send_keys('site:linkedin.com/in/ AND "python developer" AND "morocco"')
search_query.send_keys(Keys.RETURN)

linkedin_urls = driver.find_elements_by_tag_name('cite')
linkedin_urls = [url.text for url in linkedin_urls]

