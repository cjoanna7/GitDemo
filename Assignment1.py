import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,".blinkingText").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
originalText = driver.find_element(By.XPATH,"//p[@class='im-para red']").text
splitText = originalText.split()
target_character = '@'
emailID=''
for text in splitText :
    if target_character in text :
        emailID = text
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.CSS_SELECTOR,"#username").send_keys(emailID)
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("12345")
driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()
#print(driver.find_element(By.TAG_NAME,"strong").text)
time.sleep(2)
print(driver.find_element(By.XPATH,"//div[@class='alert alert-danger col-md-12']").text)
