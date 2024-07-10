from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

# Default wait time
defaultWait = 10

# Set Chrome options for headless operation
chrome_options = Options()
chrome_options.add_argument('--headless')  # Comment this out if you want to see the browser interaction

# Path for chromedriver is '/usr/local/bin/';
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

driver.get('https://www.google.com/webhp?gws_rd=ssl')

search_box = wait.until(expected_conditions.presence_of_element_located((By.NAME, 'q')))
print(search_box)

search_box.send_keys('Saju Sasidharan')
search_box.submit()

time.sleep(5)  # Let the user actually see something!

driver.quit()
