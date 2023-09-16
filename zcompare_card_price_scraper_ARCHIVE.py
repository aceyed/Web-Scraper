import time
import json
from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

app = Flask(__name__)

# Configure Chrome options
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')
#CO.add_argument('--headless')


@app.route('/check_price', methods=['POST'])
def check_price():
    try:
        # Get input values from the POST request
        pokemonName = request.form.get('pokemonName')
        pokemonNumber = request.form.get('pokemonNumber')
        pokemonSet = request.form.get('pokemonSet')

        source1 = "https://www.pricecharting.com/game/pokemon-" + pokemonSet + "/" + pokemonName + "-" + pokemonNumber

        # Initialize the WebDriver with options
        wd = webdriver.Chrome(options=CO)
        wd.get(source1)
        time.sleep(1)  # Let the user actually see something!

        try:
            f_price = wd.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/table/tbody[1]/tr[1]/td[1]/span[1]")
            pr_name = wd.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/h1")
            product = pr_name.text
            r_price = f_price.text

            # Create a dictionary with the product and price
            result = {
                "product": product,
                "price": r_price[1:]
            }

            wd.quit()

            # Return the result as JSON response
            return jsonify(result)
        except NoSuchElementException:
            wd.quit()
            return jsonify({"error": "Element not found on the page. Check if pokemon name, number, and set name are valid."})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
