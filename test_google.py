from selenium import webdriver
import pytest

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Connect to the remote Selenium instance
    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        options=options
    )
    
    yield driver
    driver.quit()

def test_google_search(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

def test_google_search_result(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys("Selenium WebDriver")
    search_box.submit()
    assert "Selenium WebDriver" in driver.title

def test_invalid_search(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys("!@#$%^&*()")
    search_box.submit()
    assert "No results found." in driver.page_source  # Adjust this based on actual result behavior

def test_page_navigation(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.find_element("link text", "Gmail").click()
    assert "Gmail" in driver.title
    driver.back()
    assert "Google" in driver.title

def test_accessibility_of_footer_links(driver):
    driver.get("https://www.google.com")
    footer_links = driver.find_elements("css selector", "footer a")
    assert len(footer_links) > 0  # Check that there are footer links

    for link in footer_links:
        assert link.is_displayed()  # Ensure all footer links are visible
