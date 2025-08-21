import time
from selenium import webdriver
from selenium.webdriver.common.by import By

name = "Rahul"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#handle java pop ups also called alerts
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept() # used to click on ok
#alert.dismiss() "is used to click on cancel"
time.sleep(2)
print("action performed")