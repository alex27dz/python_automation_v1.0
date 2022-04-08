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

from functions.generic_functions_modules import *


chromeService_obj = chromeService(ChromeDriverManager().install())
ieService_obj = ieService(IEDriverManager().install())
edgeService_obj = edgeService(EdgeChromiumDriverManager().install())
firefoxService_obj = firefoxService(GeckoDriverManager().install())
tag = 'chrome'
JM_url = "https://stage.jewelersmutual.com/"
Redirect_url = "https://httpstatus.io/"
layout_builder = "https://stage.jewelersmutual.com/user/login"

def test_34_footerToPersonalJewelryInsurance(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Personal Jewelry Insurance')
    driver.find_element_by_link_text('Personal Jewelry Insurance').click()
    time.sleep(10)
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(personal_insurance_body_validation(driver)) == 'True', 'Body elements of Personal insurance - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 34 - PASSED')
    driver.close()
def test_35_footerToGetaQuote(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Get a Quote')
    driver.find_element_by_link_text('Get a Quote').click()
    time.sleep(10)
    assert str(get_a_quote_body_validation(driver)) == 'True', 'Body elements of Get a Quote - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 35 - PASSED')
    driver.close()
def test_36_footerToFAQ(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('FAQ')
    driver.find_element_by_link_text('FAQ').click()
    time.sleep(10)
    assert str(answers_FAQ_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    # assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 36 - PASSED')
    driver.close()
def test_37_footerToManageMyPolicy(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Manage My Policy')
    driver.find_element_by_link_text('Manage My Policy').click()
    time.sleep(10)
    assert str(login_Personal_Jewelry_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 37 - PASSED')
    driver.close()
def test_38_footerToClaims(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Claims')
    driver.find_element_by_link_text('Claims').click()
    time.sleep(10)
    assert str(claims_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 38 - PASSED')
    driver.close()
def test_39_footerToPayMyBill(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Pay My Bill')
    driver.find_element_by_link_text('Pay My Bill').click()
    time.sleep(10)
    assert str(pay_my_bill_body_validation(driver)) == 'True', 'Body elements of pay my bill - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 39 - PASSED')
    driver.close()
def test_40_footerToBusinessInsurance(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Jewelry Business Insurance')
    driver.find_element_by_link_text('Jewelry Business Insurance').click()
    time.sleep(10)
    assert str(business_insurance_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 40 - PASSED')
    driver.close()
def test_41_footerToZingPlatform(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Zing® Platform')
    driver.find_element_by_link_text('Zing® Platform').click()
    time.sleep(10)
    assert str(business_zingplatform_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 41 - PASSED')
    driver.close()
def test_42_footerToJMShippingSolution(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('JM™ Shipping Solution')
    driver.find_element_by_link_text('JM™ Shipping Solution').click()
    time.sleep(10)
    assert str(business_jm_shipping_solution_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 42 - PASSED')
    driver.close()
def test_43_footerToJMCarePlan(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('JM™ Care Plan')
    driver.find_element_by_link_text('JM™ Care Plan').click()
    time.sleep(10)
    assert str(business_jmcareplan_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 43 - PASSED')
    driver.close()
def test_44_footerToJewelryAppraisalSolution(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Jewelry Appraisal Solution')
    driver.find_element_by_link_text('Jewelry Appraisal Solution').click()
    time.sleep(10)
    assert str(business_appraisalsolution_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 44 - PASSED')
    driver.close()
def test_45_footerToJMUniversity(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('JM™ University')
    driver.find_element_by_link_text('JM™ University').click()
    time.sleep(10)
    assert str(body_jmuniversity(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 45 - PASSED')
    driver.close()
def test_46_footerToJewelerPrograms(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Jeweler Programs')
    driver.find_element_by_link_text('Jeweler Programs').click()
    time.sleep(10)
    assert str(business_jewelerprograms_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 46 - PASSED')
    driver.close()
def test_47_footerToPayMyBill(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Pay My Bill')
    driver.find_element_by_link_text('Pay My Bill').click()
    time.sleep(10)
    assert str(business_paymybill_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 47 - PASSED')
    driver.close()
def test_48_footerToBusinessClaims(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Business Claims')
    driver.find_element_by_link_text('Business Claims').click()
    time.sleep(10)
    assert str(business_claims_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 48 - PASSED')
    driver.close()
def test_49_footerToBlog(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Blog')
    driver.find_element_by_link_text('Blog').click()
    time.sleep(10)
    assert str(blog_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 49 - PASSED')
    driver.close()
def test_50_footerToAboutUs(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('About Us')
    driver.find_element_by_link_text('About Us').click()
    time.sleep(10)
    assert str(aboutus_aboutus_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 50 - PASSED')
    driver.close()
def test_51_footerToCareers(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Careers')
    driver.find_element_by_link_text('Careers').click()
    time.sleep(10)
    assert str(aboutus_careers_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    # assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 51 - PASSED')
    driver.close()
def test_52_footerToNewsroom(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Newsroom')
    driver.find_element_by_link_text('Newsroom').click()
    time.sleep(10)
    assert str(aboutus_newsroom_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 52 - PASSED')
    driver.close()
def test_53_footerToSocialResponsibility(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Social Responsibility')
    driver.find_element_by_link_text('Social Responsibility').click()
    time.sleep(10)
    assert str(aboutus_socialresponsibility_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 53 - PASSED')
    driver.close()
def test_54_footerToCOVIDResources(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('COVID-19 Resources')
    driver.find_element_by_link_text('COVID-19 Resources').click()
    time.sleep(10)
    assert str(body_COVIDResources(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 54 - PASSED')
    driver.close()
def test_55_footerToContactUs(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Contact Us')
    driver.find_element_by_link_text('Contact Us').click()
    time.sleep(10)
    assert str(body_ContactUs(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 55 - PASSED')
    driver.close()
def test_56_footerToShareYourConcerns(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Share Your Concerns')
    driver.find_element_by_link_text('Share Your Concerns').click()
    time.sleep(10)
    assert str(body_ShareYourConcerns(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 56 - PASSED')
    driver.close()
def test_57_footerHomuchdoesitcosttoresizearing(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('How much does it cost to resize a ring?')
    driver.find_element_by_link_text('How much does it cost to resize a ring?').click()
    time.sleep(10)
    assert str(body_Homuchdoesitcosttoresizearing(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 57 - PASSED')
    driver.close()
def test_58_footerHowtocleangoldjewelry(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('How to clean gold jewelry the right way')
    driver.find_element_by_link_text('How to clean gold jewelry the right way').click()
    time.sleep(10)
    assert str(body_Howtocleangoldjewelry(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 58 - PASSED')
    driver.close()
def test_59_footerHowmuchshouldcost(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('How much should an appraisal cost?')
    driver.find_element_by_link_text('How much should an appraisal cost?').click()
    time.sleep(10)
    assert str(body_Howmuchshouldcost(driver)) == 'True', 'Body elements of claims - not found'
    # assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 59 - PASSED')
    driver.close()
def test_60_footerHowtomakearing(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('How to make a ring smaller without resizing')
    driver.find_element_by_link_text('How to make a ring smaller without resizing').click()
    time.sleep(10)
    assert str(body_Howtomakearing(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 60 - PASSED')
    driver.close()
def test_61_footerMoreblogarticles(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('More blog articles')
    driver.find_element_by_link_text('More blog articles').click()
    time.sleep(10)
    assert str(body_Moreblogarticles(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 61 - PASSED')
    driver.close()
def test_62_footerToPrivacyPolicy(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Privacy Policy')
    driver.find_element_by_link_text('Privacy Policy').click()
    time.sleep(10)
    assert str(body_PrivacyPolicy(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 62 - PASSED')
    driver.close()
def test_63_footerToTermsofUse(params):
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
    driver.execute_script("window.scrollTo(0,3200)")
    time.sleep(3)
    print('Terms of Use')
    driver.find_element_by_link_text('Terms of Use').click()
    time.sleep(10)
    assert str(body_TermsofUse(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 63 - PASSED')
    driver.close()
