from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def google_search(query):
    # Initialize ChromeDriver (no headless mode, no additional options)
    driver = webdriver.Chrome()
    
    # Open Google
    driver.get("https://www.google.com")
    
    # Check if the title contains "Google"
    assert "Google" in driver.title
    
    # Locate the search bar using its name attribute value
    search_box = driver.find_element(By.NAME, "q")
    
    # Enter the search query and simulate hitting 'Enter'
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for a few seconds to allow results to load
    time.sleep(2)
    
    # Verify the search results page contains the search term
    assert query in driver.page_source
    
    # Close the browser
    driver.quit()

# Run the function with a search query
google_search("Selenium WebDriver")


