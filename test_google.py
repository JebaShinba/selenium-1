import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Fixture to initialize and close the WebDriver (Chrome)
@pytest.fixture
def driver():
    # Initialize ChromeDriver
    driver = webdriver.Chrome()
    yield driver
    # Close the browser after test completion
    driver.quit()

# Test case for Google search
def test_google_search(driver):
    query = "Selenium WebDriver"
    
    # Open Google
    driver.get("https://www.google.com")
    
    # Verify that the page title contains "Google"
    assert "Google" in driver.title, "Google home page not loaded"
    
    # Locate the search bar using its name attribute value
    search_box = driver.find_element(By.NAME, "q")
    
    # Enter the search query and simulate hitting 'Enter'
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    
    # Wait for a few seconds to allow results to load
    time.sleep(2)
    
    # Verify that the results page contains the search term
    assert query in driver.page_source, f"Search term '{query}' not found in the page source"
