from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up options for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless")  # Comment this out to run in regular mode

# Path to chromedriver executable
chromedriver_path = '/usr/local/bin'  # Replace with your path

# Initialize the WebDriver instance
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# Example usage: Open a website and print its title
url = 'https://example.com'
driver.get(url)
print("Title of the page is:", driver.title)

# Close the browser
driver.quit()
