from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Your Twitter credentials
USERNAME = "your_username"
PASSWORD = "your_password"

# Initialize Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Open browser in full-screen
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open Twitter login page
driver.get("https://twitter.com/login")
time.sleep(3)  # Wait for the page to load

# Enter username
username_input = driver.find_element(By.NAME, "text")
username_input.send_keys(USERNAME)
username_input.send_keys(Keys.RETURN)
time.sleep(3)

# Enter password
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)
time.sleep(5)

# Navigate to your profile page
driver.get(f"https://twitter.com/{USERNAME}")
time.sleep(5)

# Find the like button of the latest tweet
try:
    like_button = driver.find_element(By.XPATH, "//div[@data-testid='like']")
    like_button.click()
    print("Successfully liked the latest tweet! ✅")
except:
    print("Could not find the like button. Maybe you already liked the tweet? ❌")

# Close the browser
time.sleep(5)
driver.quit()
