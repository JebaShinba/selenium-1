from selenium import webdriver

def test_google_search():
    driver = webdriver.Chrome()  # You might need to set the path to your chromedriver
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
