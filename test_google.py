from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("--disable-gpu")  # Applicable to Windows environments
chrome_options.add_argument("--window-size=1280x1024")  # Set a specific window size

# Initialize the Chrome WebDriver with these options

driver = webdriver.Chrome(options=chrome_options)

# Navigate to Google
driver.get("https://www.google.com")
print(driver.title)  # Print the title to verify that the page loaded

# Clean up and close the browser
driver.quit()
