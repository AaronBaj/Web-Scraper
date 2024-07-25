from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")

service = Service('C:\webdrivers\chromedriver.exe')

driver = webdriver.Chrome(service=service, options=chrome_options)

url = "https://bexar.tx.publicsearch.us/doc/209388995"
driver.get(url)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

total_height = driver.execute_script("return document.body.scrollHeight")

driver.set_window_size(1920, total_height)

screenshot_filename = "bexar_website_fullpage_screenshot.png"
driver.save_screenshot(screenshot_filename)

driver.quit()

print(f"Screenshot saved as {screenshot_filename}")
