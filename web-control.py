import creds
from selenium import webdriver
browser = webdriver.Safari()

url = 'https://my.forksmealplanner.com/#!/archive'
# print(creds.login['p'])
browser.get(url)

# names of the login elements
login_email_id = 'login-email'
login_pass_id = 'login-password'

# find the login elements
login_email_elem = browser.find_element_by_id(login_email_id)
login_pass_elem = browser.find_element_by_id(login_pass_id)

# login_email_elem.click()

# enter login information
login_email_elem.send_keys(creds.login['e'])
login_pass_elem.send_keys(creds.login['p'])
