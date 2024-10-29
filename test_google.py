from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BrowserAutomation:
    def __init__(self):
        """Initializes the BrowserAutomation with a webdriver instance."""
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1280x1024")
        
        self.driver = webdriver.Chrome(options=chrome_options)

    def open_page(self, url):
        """Opens a web page."""
        self.driver.get(url)
        print(f"Opened page: {url}")

    def search_in_google(self, query):
        """Performs a Google search for the specified query."""
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(query + Keys.RETURN)
        print(f"Searching for: {query}")
        time.sleep(2)

    def extract_search_results(self):
        """Extracts and prints search result titles and URLs."""
        results = self.driver.find_elements(By.CSS_SELECTOR, 'h3')
        for result in results:
            title = result.text
            link = result.find_element(By.XPATH, '..').get_attribute('href')
            print(f"Title: {title}, Link: {link}")

    def take_screenshot(self, file_name):
        """Takes a screenshot and saves it to the specified file."""
        self.driver.save_screenshot(file_name)
        print(f"Screenshot saved as: {file_name}")

    def close_browser(self):
        """Closes the browser."""
        self.driver.quit()
        print("Browser closed.")

# Example usage:
if __name__ == "__main__":
    automation = BrowserAutomation()

    # Perform actions
    automation.open_page("https://www.google.com")
    automation.search_in_google("Selenium WebDriver")
    automation.extract_search_results()
    automation.take_screenshot("screenshot.png")
    automation.close_browser()
