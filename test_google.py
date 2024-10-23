from selenium import webdriver

def test_google_search():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Connect to the remote Selenium instance
    # driver = webdriver.Remote(
    #     command_executor="http://localhost:4444/wd/hub",
    #     options=options
    driver = webdriver.Chrome() 
   

    
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
test_google_search()

