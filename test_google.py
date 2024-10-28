from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
chrome_options = Options()
# Optional: Add any arguments you want (e.g., run in headless mode)
# chrome_options.add_argument("--headless")

# Set up the Chrome driver and ensure it installs the correct version

driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Optional: Wait for a few seconds to see the page
driver.implicitly_wait(5)

# Close the driver
driver.quit()

