from selenium import webdriver

chromedriver_path = '/usr/local/bin'  

driver = webdriver.Chrome(chromedriver_path)

url = 'https://example.com'
driver.get(url)
print("Title of the page is:", driver.title)

# Close the browser
driver.quit()
