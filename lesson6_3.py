
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))

third_image_src=driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("third_image_src")

print(third_image_src)

driver.quit()
