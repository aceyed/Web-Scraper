import time
from selenium import webdriver
import getpass
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (Edge in this case)
browser_driver_path = 'D:\Ali\Downloads\edgedriver_win64\msedgedriver.exe'
edge_service = EdgeService(executable_path=browser_driver_path)
page_to_scrape = webdriver.Edge(service=edge_service)

# Navigate to Facebook
page_to_scrape.get("https://www.facebook.com")

# You should have code here to log in to Facebook
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


# Wait for the Facebook feed to load (adjust wait time as needed)
wait = WebDriverWait(page_to_scrape, 20)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='News Feed']")))

# Scroll down to load more posts (you may need to adjust this loop)
for _ in range(3):
    page_to_scrape.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Wait for more posts to load

# Find all post elements containing "to"
posts_with_to = page_to_scrape.find_elements(By.XPATH, "//div[@dir='auto' and contains(text(), 'to')]")

# Iterate through the posts and extract information
for post in posts_with_to:
    # Extract post text
    post_text = post.text
    
    # Extract user's name
    user_name_element = post.find_element(By.XPATH, ".//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1nxh6w3 x1sibtaa x1s688f xi81zsa']")
    user_name = user_name_element.text
    
    # Extract post age
    post_age_element = post.find_element(By.XPATH, ".//b[@class='xmper1u xt0psk2 xjb2p0i x1qlqyl8 x15bjb6t x1n2onr6 x17ihmo5']")
    post_age = post_age_element.text
    
    # Print the gathered information
    print("User:", user_name)
    print("Age:", post_age)
    print("Post Text:", post_text)
    print("===================================")

# Close the browser when done
page_to_scrape.quit()