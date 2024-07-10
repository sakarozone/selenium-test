from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set up Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless")  # Comment this out to run in regular mode

# Initialize the Service object with webdriver-manager
s = Service(ChromeDriverManager().install())

# Initialize the WebDriver instance with headless Chrome
driver = webdriver.Chrome(service=s, options=chrome_options)

# Maximize the window (optional)
driver.maximize_window()

# Example usage: Open Google and perform a search
driver.get('https://www.google.com')
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('Yasser Khalil')
search_box.submit()

# Print the title of the page (optional)
print("Page title is:", driver.title)

# Close the browser
driver.quit()
