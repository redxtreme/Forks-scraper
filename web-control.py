import creds
from selenium import webdriver
browser = webdriver.Safari()

url = 'https://my.forksmealplanner.com/#!/archive'
# print(creds.login['p'])
browser.get(url)
