from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Replace with the path to your webdriver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://elakiri.com/login/")

# Find the username and password input fields and enter your credentials
time.sleep(5)
username = driver.find_element(By.NAME, "login")
password = driver.find_element(By.NAME, "password")
username.send_keys("Bruh656")
password.send_keys("Sanguda123")

# Submit the form by hitting enter
password.send_keys(Keys.RETURN)

# Wait for the login process to complete and verify if login is successful
wait = WebDriverWait(driver, 10)
username_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'p-navgroup-linkText') and text()='Bruh656']")))
if "Bruh656" in username_element.text:
    print("Login successful")
else:
    print("Login failed")

# Close the browser
driver.quit()
