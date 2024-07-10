#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Set Chrome options for headless operation
chrome_options = Options()
chrome_options.add_argument('--headless')  # Comment this out if you want to see the browser interaction

# Path to chromedriver executable
chromedriver_path = '/usr/local/bin'  # Adjust this path as necessary

# Use Chrome Service object to initialize WebDriver
service = Service(chromedriver_path)

try:
    service.start()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 10)

    driver.get('https://www.google.com/webhp?gws_rd=ssl')

    search_box = wait.until(EC.presence_of_element_located((By.NAME, 'q')))
    print(search_box)

    search_box.send_keys('Saju Sasidharan')
    search_box.submit()

    time.sleep(5)  # Let the user actually see something!

finally:
    if 'driver' in locals():
        driver.quit()
    if 'service' in locals():
        service.stop()
