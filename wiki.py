from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://wikipedia.org')

elm = browser.find_element(By.CLASS_NAME, 'other-project-title.jsl10n')
elm.click()
print(browser.current_url)


