import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.edge.service import Service as EdgeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
print("Scraping script started")
logging.basicConfig(level=logging.ERROR)  # Set the logging level to ERROR
# Configure Chrome options
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
#CO.add_argument('--headless')

# Initialize the WebDriver with options and the specified executable path
wd = webdriver.Chrome(options=CO)
def handle_console_logs(driver):
    logs = driver.get_log('browser')
    for log in logs:
        if log['level'] == 'SEVERE':
            print(f"WebDriver Error: {log['message']}")
        else:
            print(f"Console Message: {log['message']}")

print("***************************************************************************\n")
print("Starting Program, Please wait .....\n")

inputPokemonName = input("Enter Pokemon Name: ")
pokemonNumber = input("\nEnter Pokemon Number: ")
inputPokemonSet = input("\nEnter Pokemon Set: ")
while True:
    if len(inputPokemonName) > 1:
        rawPokemonName = inputPokemonName.split()
        pokemonNamePC = "-".join(rawPokemonName)
        pokemonNamePD = "+".join(rawPokemonName)
        break
    elif len(inputPokemonName) == 1:
        pokemonNamePC = inputPokemonName
        pokemonNamePD = inputPokemonName
        break
    else:
        print("Invalid input, please try again.")

while True:
    if len(inputPokemonSet) > 1:
        rawPokemonSet = inputPokemonSet.split()
        pokemonSetPC = "-".join(rawPokemonSet)
        pokemonSetPD = "+".join(word.capitalize() for word in rawPokemonSet)
        break
    elif len(inputPokemonSet) == 1:
        pokemonSetPC = inputPokemonSet
        pokemonSetPD = inputPokemonSet
        break
    else:
        print("Invalid input, please try again.")


source1 = "https://www.pricecharting.com/game/pokemon-"+pokemonSetPC+"/"+pokemonNamePC+"-"+pokemonNumber
source2 = "https://www.pokedata.io/set/"+pokemonSetPD+"?f="+pokemonNamePD+"+"+pokemonNumber


print("Connecting to Price Charting")
wd.get(source1)
time.sleep(1) 
try:
    raw_price = ""
    pc_price = wd.find_element(By.ID, "used_price")
    pr_name = wd.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/h1")
    product = pr_name.text
    r_priceVar = pc_price.text
    r_priceVar = r_priceVar.strip()  # Strip whitespace from both ends of the string
    r_price = r_priceVar.split()[0]  # Split the string by space and take the first part
    print(r_priceVar)
    print(r_price)
    print(" ---> Successfully retrieved the price from Price Charting\n")
    time.sleep(0.5) 
except NoSuchElementException:
    print("Element not found on the page. Check if pokemon name, number and set name are valid.")


print("Connecting to PokeData")
wd.get(source2)
time.sleep(1)  

try:
    time.sleep(2) 
    raw_price = ""
    pd_price = wd.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[3]/div[2]/div/div/div[2]/a/div[3]/span")
    raw_price = pd_price.text

    print(" ---> Successfully retrieved the price from PokeData\n")
except NoSuchElementException:
    print("Element not found on the page. Check if pokemon name, number and set name are valid.")


print("#------------------------------------------------------------------------#")
print("Price in USD for [{}] on all websites\n".format(product))

if len(r_price) > 0:
    print("Price available at Price Charting is: " + r_price)
else:
    print("No price available at Price Charting")
if len(raw_price) > 0:
    print("Price available at PokeData is: " + raw_price)
else:
    print("No price available at PokeData")
r_priceNum = float(r_price.replace("$", ""))
raw_priceNum = float(raw_price.replace("$", ""))
priceTotal = 0.00
priceTotal = (raw_priceNum + r_priceNum) /2
print(f"The average price for "+product+f" is: ${priceTotal:.2f}")
#wd.quit()
print("Scraping script finished")


