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

from functions.business_functions import *

chromeService_obj = chromeService(ChromeDriverManager().install())
ieService_obj = ieService(IEDriverManager().install())
edgeService_obj = edgeService(EdgeChromiumDriverManager().install())
firefoxService_obj = firefoxService(GeckoDriverManager().install())

tag = 'chrome'
JM_url = "https://stage.jewelersmutual.com/"
Redirect_url = "https://httpstatus.io/"
layout_builder = "https://stage.jewelersmutual.com/user/login"

def test_07_BusinessToBusinessInsurance(params):
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access BusinessInsurance')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Business Insurance').click()
    time.sleep(10)
    assert str(business_insurance_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 07 - PASSED')
    driver.close()
def test_08_BusinessToClaims(params):
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Businessclaims')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Claims').click()
    time.sleep(10)
    assert str(business_claims_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    # assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 08 - PASSED')
    driver.close()
def test_09_BusinessToPayMyBill(params):
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access PayMyBill')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Pay My Bill').click()
    time.sleep(10)
    assert str(business_paymybill_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    # assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    # assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 09 - PASSED')
    driver.close()
def test_10_BusinessToZingPlatform(params):
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Zing Platform')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Zing Platform').click()
    time.sleep(10)
    assert str(business_zingplatform_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 10 - PASSED')
    driver.close()
def test_11_BusinessToShippingSolution(params):
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access JM Shipping Solution')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('JM Shipping Solution').click()
    time.sleep(10)
    assert str(business_jm_shipping_solution_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    # assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 11 - PASSED')
    driver.close()
def test_12_BusinessToJmCarePlan(params):
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access JM Care Plan')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('JM Care Plan').click()
    time.sleep(10)
    assert str(business_jmcareplan_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 12 - PASSED')
    driver.close()
def test_13_BusinessToAppraisalSolution(params):
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Appraisal Solution')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Appraisal Solution').click()
    time.sleep(10)
    assert str(business_appraisalsolution_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 13 - PASSED')
    driver.close()
def test_14_BusinessToJewelerPrograms(params):
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access JewelerPrograms')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Jeweler Programs').click()
    time.sleep(10)
    assert str(business_jewelerprograms_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 14 - PASSED')
    driver.close()
def test_15_BusinessToPawnbrokers(params):
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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header")))
    print('verify navbar and footer')
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.execute_script("window.scrollTo(0,0)")
    print('Access Pawnbrokers')
    url = '/jewelry-business-jewelers-block-bop-insurance'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Pawnbrokers').click()
    time.sleep(10)
    assert str(business_pawnbrokers_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 15 - PASSED')
    driver.close()
