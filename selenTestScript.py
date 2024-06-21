from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# time.sleep(10)

chrome_options = webdriver.ChromeOptions()

# Keeps browser open
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options = chrome_options)
driver.get("http://www.google.com")

# Searches for q element, which in this case is query (can be quote)
query_entry = driver.find_element(by=By.NAME, value='q')


# print(query_entry.text)

# Submits the entry 'ZS Associates' into the search bar and enters it
query_entry.send_keys('ZS Associates')
query_entry.send_keys(Keys.RETURN)

# Searches for CSS element with h3 tag (search results) and clicks it
top_result = driver.find_element(by=By.CSS_SELECTOR, value='h3').click()

# Quits the driver, closing the browser
driver.quit()