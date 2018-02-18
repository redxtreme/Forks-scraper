import creds
import pyautogui
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Navigate to where the files will be stored
os.chdir(creds.myPath)

# gui elements
width, height = pyautogui.size()
pyautogui.PAUSE = 5
pyautogui.FAILSAFE = True

browser = webdriver.Safari()

url = 'https://my.forksmealplanner.com/#!/archive'

browser.get(url)

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
    time.sleep(5)
    download_selector = '.print-recipe-button.ladda-button'
    download_elem = browser.find_element_by_css_selector(download_selector)
    download_elem.click()
    clickPdfButton()

def clickPdfButton():
    time.sleep(5)
    buttonX, buttonY = (118, 700)
    pyautogui.click(buttonX, buttonY)
    buttonX, buttonY = (118, 742)
    pyautogui.click(buttonX, buttonY)
    buttonX, buttonY = (685, 780)
    pyautogui.click(buttonX, buttonY)

login()
menu_elems = getMenuLinks()
for i in range(2):
    menu_elems[i].click()
    downloadMenu()
    os.rename('Untitled.pdf', menu_elems[i].text + '.pdf')
    browser.back()
    time.sleep(5)
