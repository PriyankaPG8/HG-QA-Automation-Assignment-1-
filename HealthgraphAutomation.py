import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# to open a chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# navigate to the website
driver.get("https://openweathermap.org")
time.sleep(10)

# allow the cookies
driver.find_element_by_xpath('//*[@id="stick-footer-panel"]/div/div/div/div/div/button').click()
driver.implicitly_wait(5)

# Enter the wrong city name and click submit
# City name
driver.find_element_by_css_selector("input.form-control:nth-child(2)").send_keys("fdagfasgasg")
# click submit button
driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div/div[2]/div/form/button").click()
message = driver.find_element_by_xpath('/html/body/main/div[4]/div/div/div/div/div').text
errorMessage = message.splitlines()
# verified whether it has invalid city or not
assert errorMessage[1] == "Not found", "Enter the incorrect city"
time.sleep(5)

# Enter the correct city name and click submit
# clear the previous text
driver.find_element_by_id("search_str").clear()
# enter the valid city
driver.find_element_by_id("search_str").send_keys("Mumbai")
# click submit button
driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div/form/button").click()

# get the temperature
temperature = driver.find_element_by_xpath("/html/body/main/div[4]/div/div/div/div/table/tbody/tr/td[2]/p[1]").text
print temperature
mumbai = temperature.split(",")
# split the temperature to verify whether it shows the temperature details or not
split_value = mumbai[1].startswith("wind", 1)
assert split_value == True, 'Enter the correct city'
time.sleep(3)

# Sign in the portal
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/a[3]").click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "user_email")))
# enter invalid email and password
driver.find_element_by_id("user_email").send_keys("egdgagasgas")
driver.find_element_by_id("user_password").send_keys("fafasfasfasg" + Keys.ENTER)

# wait until that element is located on the present page
alert = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div["
                                                                                  "3]/div/div/div/div[2]"))).text
# to check the condition whether it has invalid credentials or not
assert alert == "Invalid Email or password.", "enter invalid credentials"

# to close the browser
driver.quit()
