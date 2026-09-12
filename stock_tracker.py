# Stock Portfolio Tracker
# B.Tech 1st Year Mini Project

# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 330,
    "INFY": 18,
    "TCS": 40
}

def show_available_stocks():
    print("\nAvailable Stocks and Prices:")
    print("-" * 30)
    for stock, price in stock_prices.items():
        print(f"{stock:<10} Rs.{price}")
    print("-" * 30)

def get_user_portfolio():
    portfolio = {}
    n = int(input("\nHow many different stocks do you want to add? "))

    for i in range(n):
        print(f"\nStock {i + 1}:")
        name = input("Enter stock name (e.g., AAPL): ").upper()

        if name not in stock_prices:
            print(f"'{name}' not found in our price list. Skipping...")
            continue

        qty = int(input(f"Enter quantity of {name}: "))
        portfolio[name] = portfolio.get(name, 0) + qty

    return portfolio

def calculate_total(portfolio):
    total = 0
    details = []

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total += value
        details.append((stock, qty, price, value))

    return total, details

def display_summary(details, total):
    print("\n" + "=" * 45)
    print("PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"{'Stock':<10}{'Qty':<8}{'Price':<10}{'Value':<10}")
    print("-" * 45)

    for stock, qty, price, value in details:
        print(f"{stock:<10}{qty:<8}{price:<10}{value:<10}")

    print("-" * 45)
    print(f"TOTAL INVESTMENT: Rs.{total}")
    print("=" * 45)

def save_to_file(details, total):
    choice = input("\nDo you want to save this report? (y/n): ").lower()

    if choice != 'y':
        return

    file_format = input("Save as (1) .txt or (2) .csv? Enter 1 or 2: ")

    if file_format == "1":
        filename = "portfolio_report.txt"
        with open(filename, "w") as f:
            f.write("PORTFOLIO SUMMARY\n")
            f.write("=" * 45 + "\n")
            f.write(f"{'Stock':<10}{'Qty':<8}{'Price':<10}{'Value':<10}\n")
            f.write("-" * 45 + "\n")
            for stock, qty, price, value in details:
                f.write(f"{stock:<10}{qty:<8}{price:<10}{value:<10}\n")
            f.write("-" * 45 + "\n")
            f.write(f"TOTAL INVESTMENT: Rs.{total}\n")
        print(f"Report saved as '{filename}'")

    elif file_format == "2":
        filename = "portfolio_report.csv"
        with open(filename, "w") as f:
            f.write("Stock,Quantity,Price,Value\n")
            for stock, qty, price, value in details:
                f.write(f"{stock},{qty},{price},{value}\n")
            f.write(f"Total,,,{total}\n")
        print(f"Report saved as '{filename}'")

    else:
        print("Invalid choice. Report not saved.")

def main():
    print("=" * 45)
    print("   WELCOME TO STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    show_available_stocks()
    portfolio = get_user_portfolio()

    if not portfolio:
        print("\nNo valid stocks entered. Exiting.")
        return

    total, details = calculate_total(portfolio)
    display_summary(details, total)
    save_to_file(details, total)

    print("\nThank you for using Stock Portfolio Tracker!")

if __name__ == "__main__":
    main()
