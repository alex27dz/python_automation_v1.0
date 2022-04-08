from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.edge.service import Service as edgeService
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.ie.service import Service as ieService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import (EdgeChromiumDriverManager,
                                         IEDriverManager) 

from packagesToPath import *
addToPath()

from functions.body_functions import *

chromeService_obj = chromeService(ChromeDriverManager().install())
ieService_obj = ieService(IEDriverManager().install())
edgeService_obj = edgeService(EdgeChromiumDriverManager().install())
firefoxService_obj = firefoxService(GeckoDriverManager().install())

tag = 'chrome'
JM_url = "https://stage.jewelersmutual.com/"
Redirect_url = "https://httpstatus.io/"
layout_builder = "https://stage.jewelersmutual.com/user/login"


def test_25_BodyToPersonalInsurance(params):
    if params['browser'] == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
        print('working with Chrome')
    else:
        if params['browser'] == 'ie':
            driver = webdriver.Ie(service=ieService_obj)
            print('working with IE')
        else:
            if params['browser'] == 'edge':
                driver = webdriver.Edge(service=edgeService_obj)
                print('working with EDGE')
            else:
                driver = webdriver.Firefox(service=firefoxService_obj)
                print('working with FireFox')

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(3)
    print('Access Personal Insurance')
    driver.find_element_by_partial_link_text(
        'EXPLORE PERSONAL JEWELRY INSURANCE').click()
    time.sleep(10)
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(personal_insurance_body_validation(driver)
               ) == 'True', 'Body elements of Personal insurance - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 25 - PASSED')
    driver.quit() 
def test_26_BodyToLogIn(params):
    if params['browser'] == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
        print('working with Chrome')
    else:
        if params['browser'] == 'ie':
            driver = webdriver.Ie(service=ieService_obj)
            print('working with IE')
        else:
            if params['browser'] == 'edge':
                driver = webdriver.Edge(service=edgeService_obj)
                print('working with EDGE')
            else:
                driver = webdriver.Firefox(service=firefoxService_obj)
                print('working with FireFox')

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
    print('Access Log in')
    driver.find_element_by_partial_link_text('Log in').click()
    time.sleep(10)
    assert str(login_Personal_Jewelry_body_validation(driver)
               ) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 26 - PASSED')
    driver.quit() 
def test_27_BodyToRegisterForAnOnlineAccount(params):
    if params['browser'] == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
        print('working with Chrome')
    else:
        if params['browser'] == 'ie':
            driver = webdriver.Ie(service=ieService_obj)
            print('working with IE')
        else:
            if params['browser'] == 'edge':
                driver = webdriver.Edge(service=edgeService_obj)
                print('working with EDGE')
            else:
                driver = webdriver.Firefox(service=firefoxService_obj)
                print('working with FireFox')

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
    print('Access BodyToRegisterForAnOnlineAccount')
    driver.find_element_by_partial_link_text(
        'Register for an online account').click()
    # stopped here
    time.sleep(10)
    assert str(body_ToRegisterForAnOnlineAccount(driver)
               ) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 27 - PASSED')
    driver.quit() 
def test_28_BodyToAddanitemtomyPolicy(params):
    if params['browser'] == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
        print('working with Chrome')
    else:
        if params['browser'] == 'ie':
            driver = webdriver.Ie(service=ieService_obj)
            print('working with IE')
        else:
            if params['browser'] == 'edge':
                driver = webdriver.Edge(service=edgeService_obj)
                print('working with EDGE')
            else:
                driver = webdriver.Firefox(service=firefoxService_obj)
                print('working with FireFox')

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
    print('Access Add an item to my policy')
    driver.find_element_by_partial_link_text(
        'Add an item to my policy').click()
    time.sleep(10)
    assert str(login_Personal_Jewelry_body_validation(driver)
               ) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 28 - PASSED')
    driver.quit() 

def test_29_BodyTopaymybill(params):
    if params['browser'] == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
        print('working with Chrome')
    else:
        if params['browser'] == 'ie':
            driver = webdriver.Ie(service=ieService_obj)
            print('working with IE')
        else:
            if params['browser'] == 'edge':
                driver = webdriver.Edge(service=edgeService_obj)
                print('working with EDGE')
            else:
                driver = webdriver.Firefox(service=firefoxService_obj)
                print('working with FireFox')

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
    print('Access Pay My Bill')
    driver.find_element_by_partial_link_text('Pay My Bill').click()
    time.sleep(10)
    assert str(pay_my_bill_body_validation(driver)
               ) == 'True', 'Body elements of pay my bill - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 29 - PASSED')
    driver.quit() 

def test_31_BodyToLearnaboutclaims(params):
    if params['browser'] == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
        print('working with Chrome')
    else:
        if params['browser'] == 'ie':
            driver = webdriver.Ie(service=ieService_obj)
            print('working with IE')
        else:
            if params['browser'] == 'edge':
                driver = webdriver.Edge(service=edgeService_obj)
                print('working with EDGE')
            else:
                driver = webdriver.Firefox(service=firefoxService_obj)
                print('working with FireFox')

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,300)")
    time.sleep(3)
    print('Learn about claims')
    driver.find_element_by_partial_link_text('Learn about claims').click()
    time.sleep(10)
    assert str(claims_body_validation(driver)
               ) == 'True', 'Body elements of claims - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 31 - PASSED')
    driver.quit() 

def test_32_BodyToGetaquoteformultipleItems(params):
    if params['browser'] == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
        print('working with Chrome')
    else:
        if params['browser'] == 'ie':
            driver = webdriver.Ie(service=ieService_obj)
            print('working with IE')
        else:
            if params['browser'] == 'edge':
                driver = webdriver.Edge(service=edgeService_obj)
                print('working with EDGE')
            else:
                driver = webdriver.Firefox(service=firefoxService_obj)
                print('working with FireFox')

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,400)")
    time.sleep(3)
    print('Get a quote for multiple items')
    driver.find_element_by_partial_link_text(
        'Get a quote for multiple items').click()
    time.sleep(10)
    assert str(get_a_quote_body_validation(driver)
               ) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 32 - PASSED')
    driver.quit() 

def test_33_BodyToExplorePersonalJewelryInsurance(params):
    if params['browser'] == 'chrome':
        driver = webdriver.Chrome(service=chromeService_obj)
        print('working with Chrome')
    else:
        if params['browser'] == 'ie':
            driver = webdriver.Ie(service=ieService_obj)
            print('working with IE')
        else:
            if params['browser'] == 'edge':
                driver = webdriver.Edge(service=edgeService_obj)
                print('working with EDGE')
            else:
                driver = webdriver.Firefox(service=firefoxService_obj)
                print('working with FireFox')

    driver.get(JM_url)
    driver.maximize_window()
    time.sleep(3)
    print('Access HomePage')
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,800)")
    time.sleep(3)
    print('EXPLORE PERSONAL JEWELRY INSURANCE')
    driver.find_element_by_partial_link_text(
        'EXPLORE PERSONAL JEWELRY INSURANCE').click()
    time.sleep(10)
    assert str(personal_insurance_body_validation(driver)
               ) == 'True', 'Body elements of claims - not found'
    assert str(footer_validation(driver)
               ) == 'True', 'Footer elements - not found'
    assert str(navbar_validation(driver)
               ) == 'True', 'Navbar elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 33 - PASSED')
    driver.quit() 