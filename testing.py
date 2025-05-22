# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# # Set up ChromeDriver
# driver = webdriver.Chrome() # Ensure chromedriver is in your PATH
# driver.get("https://www.aljazeera.com")
# print("Title:", driver.title)
# # Example: Click on a menu link
# try:
#         link = driver.find_element(By.LINK_TEXT, "Podcasts")
#         link.click()
#         print("Navigation to 'Aljazeera' succeeded ")
# except:
#         print("Navigation failed ")
        
# driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up ChromeDriver
driver = webdriver.Chrome()
driver.get("https://www.aljazeera.com")
print("Title:", driver.title)

try:
    wait = WebDriverWait(driver, 10)
    more_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'More')]")))

    ActionChains(driver).move_to_element(more_menu).perform()

    podcasts_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Interactives")))
    podcasts_link.click()

    print("Navigation to 'Interactives' succeeded")

except Exception as e:
    print("Navigation failed:", e)

driver.quit()
