# Web-Scraper
Web scraper project. The project is designed to retrieve the price of a Pokémon card based on user input. The user can provide the name, number, and set of the Pokémon card they are interested in. The code then uses Selenium to automate the process of navigating to the website, entering the user’s input, and retrieving the price information.

1. "static" directory contains index.html and script.js files. Run app.py to view website on local machine.

2. Below is the initial webpage
![image](https://github.com/aceyed/Web-Scraper/assets/121588657/e53ef478-9096-49ae-aa1d-3760ff8102d9)

3. User enters pokemon card name, number and set name. Clicks "Check Price".  
![image](https://github.com/aceyed/Web-Scraper/assets/121588657/9c288d87-5ba9-4aed-a9af-4cf7f4987d1d)

4. On backend, input data validation, site url construction and web scraping of price and card data is occuring while
fetching the price

5. Finally, the price from the 2 websites are displayed as well as the average cost. 
![image](https://github.com/aceyed/Web-Scraper/assets/121588657/fe6afa41-401e-413a-ac33-14375690d021)

Here’s a breakdown of how the code works:

The Flask app is initialized with a static folder for serving HTML files.

The root route (“/”) returns the index.html file.

The “/get_pokemon_price” route is responsible for handling the Pokémon card price retrieval.

User input is retrieved from the query parameters.

ChromeOptions are set to configure the WebDriver.

A Chrome WebDriver instance is created with the specified options.

The code enters a loop to handle user input validation and formatting.

The Pokémon name and set are split and joined to match the required format for searching on the website.

Another loop handles input validation and formatting for the Pokémon set.

The WebDriver navigates to the website and performs the scraping logic.

The scraped data is returned as a response.

This project demonstrates how to use Flask, Selenium, and Chrome WebDriver to build a web scraping application that can retrieve specific information from websites based on user input.
