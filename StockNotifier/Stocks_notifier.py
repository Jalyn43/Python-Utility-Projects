import os
import requests
from plyer import notification
from config import API_KEY
# from win11toast import toast

#get stock data from Alpha Vantage
def get_stock_data(symbol):
    alpha_vantage_url = f"https://www.alphavantage.co/query"
    function = "GLOBAL_QUOTE"
    
# parameters for the api request
    params = {
        "function": function,
        "symbol": symbol,
        "apikey": API_KEY,
    }
# api request and get reponse in JSON format
    response = requests.get(alpha_vantage_url, params=params)
    data = response.json()
    
# function to ensure stock data in api is correct
    if "Global Quote" in data:
        return data["Global Quote"]
    else:
        return None

# Function to check the stock price and notify the user
def check_stock_price(symbol, threshold):
	#get stock data for a specific symbol
    stock_data = get_stock_data(symbol)

#check to see if stock data is available
    if stock_data:
		#get current stock price from api
        current_price = float(stock_data["05. price"])
        
        if current_price < threshold:
            message = f"{symbol} stock price is below {threshold}. Current price: {current_price}"
            notification.notify(
                title="Stock Price Alert",
                message=message,
                app_name="Stock Notifier",
                timeout=15,
            )
            print(message)
        else:
            print(f" Sorry {symbol} stock price is above {threshold}. Current price: {current_price}")
    else:
        print(f"Unable to retrieve data for {symbol}")
#function to restart program
def main():
 while True:
# user input for stock symbol and price threshold
    stock_symbol = input("Enter the stock symbol (e.g., AAPL): ").upper()
    price_threshold = float(input("Enter the price threshold: "))

# Check stock price and notify the user
    check_stock_price(stock_symbol, price_threshold)

 # Ask the user if they want to restart the program
    restart_choice = input("Do you want to restart the program? (yes/no): ").lower()
    if restart_choice != "yes":
     print("Program terminated.")
     break

if __name__ == "__main__":
    main()
