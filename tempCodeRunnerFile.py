            # Assign values to price_charting_price and poke_data_price
            
            price_charting_price = r_price
            poke_data_price = raw_price

            # Calculate average price
            r_priceNum = float(r_price.replace("$", ""))
            raw_priceNum = float(raw_price.replace("$", ""))
            average_price = (raw_priceNum + r_priceNum) / 2

            # Create a JSON response
            response_data = {
                "priceChartingPrice": price_charting_price,
                "pokeDataPrice": poke_data_price,
                "averagePrice": average_price,
            }
            print(" ---> Successfully created json response\n")
            return jsonify(response_data)