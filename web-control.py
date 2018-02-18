import creds
import pyautogui
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# login to the website
def login():
    time.sleep(5)
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

# Get all of the menu elements
def getMenuLinks():
    time.sleep(5)
    menu_item_selector = '''.callout.favorite-action-panel > :last-child, .callout.free-guide > :last-child, .callout.grocery-list-dismissable-tip > :last-child, .callout.grocery-list-panel > :last-child, .callout.meal-plan-panel > :last-child, .callout.mobile-tip > :last-child, .callout.notes > :last-child, .callout.pantry-items > :last-child, .callout.plan-panel > :last-child, .callout.prep-ahead-alert-box > :last-child, .callout.prep-ahead-panel > :last-child, .callout.preptime-panel > :last-child, .callout.print-panel > :last-child, .callout.servings-panel > :last-child, .callout.tooltip-edamam > :last-child, .callout.unauthorized-notes > :last-child, .favorite-action-panel > :last-child, .free-guide > :last-child, .grocery-list-dismissable-tip > :last-child, .grocery-list-panel > :last-child, .meal-plan-panel > :last-child, .mobile-tip > :last-child, .notes > :last-child, .panel.callout > :last-child, .panel > :last-child, .pantry-items > :last-child, .plan-panel > :last-child, .prep-ahead-alert-box > :last-child, .prep-ahead-panel > :last-child, .preptime-panel > :last-child, .print-panel > :last-child, .servings-panel > :last-child, .tooltip-edamam > :last-child, .unauthorized-notes > :last-child'''
    menu_elems = browser.find_elements_by_css_selector(menu_item_selector)
    return menu_elems

# Download the menu on the page
def downloadMenu():
    time.sleep(6)
    download_selector = '.print-recipe-button.ladda-button'
    download_elem = browser.find_element_by_css_selector(download_selector)
    download_elem.click()
    clickPdfButton()

def clickPdfButton():
    time.sleep(7)
    buttonX, buttonY = (118, 700)
    pyautogui.click(buttonX, buttonY)
    buttonX, buttonY = (118, 742)
    pyautogui.click(buttonX, buttonY)
    buttonX, buttonY = (685, 780)
    pyautogui.click(buttonX, buttonY)

def find(name):
    name += '.pdf'
    if name in files:
        return True
    return False

def main(menu_elems) :
    for i in range(start_at, len(menu_elems)):

        # scroll to element row above this element, to make sure it's in view
        if i >= 2:
            browser.execute_script("arguments[0].scrollIntoView();", menu_elems[i-2])

        # skip if we have this file
        if find(menu_elems[i].text):
            print(i)
            continue

        menu_elems = getMenuLinks()
        menu_elems[i].click()
        downloadMenu()
        os.rename('Untitled.pdf', menu_elems[i].text + '.pdf')
        browser.back()
        print(i)

# Navigate to where the files will be stored
os.chdir(creds.myPath)

# gui elements
width, height = pyautogui.size()
pyautogui.PAUSE = 3 # Time between clicks
pyautogui.FAILSAFE = True # Top left corner safety

browser = webdriver.Safari()

url = 'https://my.forksmealplanner.com/#!/archive'

# Load page
browser.get(url)

# init vars
start_at = 0
files = os.listdir()

login()
time.sleep(5)
htmlElem = browser.find_element_by_tag_name('html')

# Scroll to the bottom to load all the elements into view
for i in range(6):
    htmlElem.send_keys(Keys.END)
    time.sleep(3)
    print('scrolling')

# Scroll to the top to get the top elements in view
for i in range(2):
    htmlElem.send_keys(Keys.HOME)
    time.sleep(3)
    print('scrolling')

# Get all the elements
menu_elems = getMenuLinks()
print(len(menu_elems))
main(menu_elems)
