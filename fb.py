from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome('C:\Users\Pritam Ahire\PycharmProjects\pythonProject\venv\Scripts\chromedriver.exe')
browser.get('http://www.google.com/');
"""uname = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")

submit = browser.find_element_by_id("login")

uname.send_keys('pritam.ahire@gmail.com')
password.send_keys('Test')
"""
