from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# Enable headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# Replace with the path to your webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the login page
driver.get("https://elakiri.com/login/")

# Find the username and password input fields and enter your credentials
time.sleep(5)
username = driver.find_element(By.NAME, "login")
password = driver.find_element(By.NAME, "password")
username.send_keys("Bruh656")
password.send_keys("NOT_GIVING_YOU_MY_PASSWORD")

# Submit the form by hitting enter
password.send_keys(Keys.RETURN)

# Wait for the login process to complete and verify if login is successful
wait = WebDriverWait(driver, 10)
username_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'p-navgroup-linkText') and text()='Bruh656']"))) #sometimes it says login failed even after the program successfully logged into the account. idk how to fix that if you know please do :)
if "Bruh656" in username_element.text:
    print("Login successful")
else:
    print("Login failed")
time.sleep(5)

# Navigate to the thread page
driver.get("https://elakiri.com/threads/esana-news.2098507/")

# Find the reply editor and enter your message
reply_editor = driver.find_element(By.XPATH, "//div[@class='fr-element fr-view']")

#opening the json file
with open("data.json", "r") as f:
    data = json.load(f)

message = f'''[IMG]{data["image_url"]}[/IMG]\n
{data["time"]}\n\n
[B][SIZE=7]{data["title"]}[/B][/SIZE]\n\n
{data["description"]}\n\n'''

reply_editor.send_keys(message)

# Submit the reply by hitting the Enter key
reply_editor.send_keys(Keys.CONTROL, Keys.RETURN)

# Wait for the reply to be posted and verify if it was successful
wait = WebDriverWait(driver, 10)
if driver.find_element(By.XPATH, "//a[@href='/misc/location-info?location=Kaluthara']"):
    print("Reply posted successfully")
else:
    print("Reply failed to post")

# Close the browser
time.sleep(10)
driver.quit()
