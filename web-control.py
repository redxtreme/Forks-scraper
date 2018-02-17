import creds
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Safari()

url = 'https://my.forksmealplanner.com/#!/archive'

browser.get(url)

# login to the website
def login():
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

    # submit creds to login
    login_pass_elem.send_keys(Keys.RETURN)

def getMenuLinks():
    menu_item_selector = '.panel-inner .description.no-subtitle h3'
    menu_elems = browser.find_elements_by_css_selector(menu_item_selector)
    return menu_elems
    
login()
menu_elems = getMenuLinks()
