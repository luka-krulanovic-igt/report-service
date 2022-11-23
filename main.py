from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from vars import var

url = f"http://{var}/Reports/login.aspx"

driver = webdriver.Chrome(r'C:\bin\chromedriver.exe')
driver.get(url)

time.sleep(3)

username = driver.find_element_by_id('txtUsername')
username.send_keys('opcore')

password = driver.find_element_by_id('txtPassword')
password.send_keys('opcore')

form = driver.find_element_by_id('cmdLogIn').click()

new_request = driver.find_element_by_id('cmdNewRequest').click()

report = driver.find_element_by_id('DataGrid1__ctl3_Checkbox1').click()
next = driver.find_element_by_id('cmdNext').click()
create = driver.find_element_by_id('cmdFinish').click()