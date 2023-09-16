# Import necessary libraries
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import getpass
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.edge.service import Service as EdgeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set the path to the Microsoft Edge WebDriver executable
browser_driver_path = 'D:\Ali\Downloads\edgedriver_win64\msedgedriver.exe'

# Create a Microsoft Edge WebDriver service instance
edge_service = EdgeService(executable_path=browser_driver_path)

# Create a Microsoft Edge WebDriver instance using the service
page_to_scrape = webdriver.Edge(service=edge_service)
page_to_scrape.get("https://www.facebook.com/?stype=lo&jlou=Afdm7ffjsB5-ZfBpY6y_gGQErcC_uARI-nsuzH-VnVm_eB56N8sBSotRwKiJoMQKq_9A4pLizPVy4Kp2i_YwZDv81YAXtQGUVEsfAE9M8g78Dg&smuh=7123&lh=Ac_tADudvnffSJHjxYQ")
'''
# Click the "Login" link
login_button = page_to_scrape.find_element(By.ID, "u_0_5_7x")
login_button.click()
'''
# Wait for a few seconds (3 seconds in this case)
time.sleep(3)

# Find and interact with the username and password fields
username = page_to_scrape.find_element(By.ID, "email")
password = page_to_scrape.find_element(By.ID, "pass")
username.send_keys("fieryvenom3@hotmail.com")
# Wait for the password input field to be clickable
password_input = WebDriverWait(page_to_scrape, 10).until(
    EC.element_to_be_clickable((By.ID, "pass"))
)
# Get the password securely (masked input)
my_pass = getpass.getpass()
password.send_keys(my_pass)

# Click the "Login" link
login_button = page_to_scrape.find_element(By.ID, "u_0_5_7x")
login_button.click()

wait = WebDriverWait(page_to_scrape, 10)
wait.until(EC.presence_of_element_located((By.ID, "some_element_on_the_next_page")))

# Locate the span element containing the link text
span_element = page_to_scrape.find_element(By.XPATH, "//span[contains(text(), 'Pokemon Cards Canada : Buy and Sell')]")

# Click the span element to follow the link
span_element.click()

# Wait for the page to load (you can adjust the wait time as needed)
time.sleep(5)

# Find all elements that contain the text "mudkip"
elements_with_mudkip = page_to_scrape.find_elements(By.XPATH, "//*[contains(text(), 'mudkip')]")

# Iterate through the elements and print their text
for element in elements_with_mudkip:
    print(element.text)


'''
# Find elements representing quotes and authors
quotes = page_to_scrape.find_elements(By.CLASS_NAME, "text")
authors = page_to_scrape.find_elements(By.CLASS_NAME, "author")

# Open a CSV file for writing
file = open("scraped_quotes.csv", "w", newline='')
writer = csv.writer(file)

# Write headers to the CSV file
writer.writerow(["QUOTES", "AUTHORS"])

# Start a loop to scrape quotes and authors from multiple pages
while True:
    quotes = page_to_scrape.find_elements(By.CLASS_NAME, "text")
    authors = page_to_scrape.find_elements(By.CLASS_NAME, "author")
    
    # Iterate through quotes and authors, print and write them to the CSV file
    for quote, author in zip(quotes, authors):
        print(quote.text + " - " + author.text)
        writer.writerow([quote.text, author.text])
    
    try:
        # Click the "Next" link to move to the next page of quotes
        page_to_scrape.find_element(By.PARTIAL_LINK_TEXT, "Next").click()
    except NoSuchElementException:
        # Exit the loop when there are no more "Next" links
        break

# Close the CSV file
file.close()
'''