from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time

@pytest.fixture(scope="module")
def setup_driver():
    # Initialize ChromeDriver
    driver = webdriver.Chrome()
    yield driver  # Yield the driver to the test function
    driver.quit()  # Close the driver after tests are done

def test_google_search(setup_driver):
    driver = setup_driver
    query = "Geeks for Geeks"

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




