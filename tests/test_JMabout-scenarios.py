from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.edge.service import Service as edgeService
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.ie.service import Service as ieService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import (EdgeChromiumDriverManager,
                                         IEDriverManager)
from conftest import *

from packagesToPath import *
addToPath()

from functions.about_functions import *

chromeService_obj = chromeService(ChromeDriverManager().install())
ieService_obj = ieService(IEDriverManager().install())
edgeService_obj = edgeService(EdgeChromiumDriverManager().install())
firefoxService_obj = firefoxService(GeckoDriverManager().install())

JM_url = "https://stage.jewelersmutual.com/"
Redirect_url = "https://httpstatus.io/"
layout_builder = "https://stage.jewelersmutual.com/user/login"


def test_18_AboutUsToAboutUs(params):
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
    print('Access About Us')
    url = '/jewelry-insurance-101'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('About Us').click()
    time.sleep(10)
    assert str(aboutus_aboutus_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 18 - PASSED')
    driver.quit() 
def test_19_AboutUsToSocialResponsibility(params):
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
    print('Access SocialResponsibility')
    url = '/jewelry-insurance-101'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Social Responsibility').click()
    time.sleep(10)
    assert str(aboutus_socialresponsibility_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 19 - PASSED')
    driver.quit() 
def test_20_AboutUsToCareers(params):
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
    print('Access Careers')
    url = '/jewelry-insurance-101'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Careers').click()
    time.sleep(10)
    assert str(aboutus_careers_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    # assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 20 - PASSED')
    driver.quit() 
def test_21_AboutUsToNewsroom(params):
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
    print('Access Newsroom')
    url = '/jewelry-insurance-101'
    driver.find_element_by_xpath('//a[@href="' + url + '"]').click()
    time.sleep(3)
    driver.find_element_by_link_text('Newsroom').click()
    time.sleep(10)
    assert str(aboutus_newsroom_body_validation(driver)) == 'True', 'Body elements of claims - not found'
    assert str(navbar_validation(driver)) == 'True', 'Navbar elements - not found'
    assert str(footer_validation(driver)) == 'True', 'Footer elements - not found'
    driver.back()
    time.sleep(3)
    print('SCENARIO - 21 - PASSED')
    driver.quit() 