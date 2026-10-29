import csv
import os

def track_portfolio():
    # Sample mock current market prices for simulation
    current_prices = {
        "AAPL": 185.50,
        "TSLA": 240.25,
        "GOOGL": 140.10,
        "MSFT": 415.00,
        "AMZN": 175.80
    }

    portfolio = []
    
    print("=== STOCK PORTFOLIO PERFORMANCE TRACKER ===")
    print("Enter your holdings (Type 'done' when finished):")

    while True:
        ticker = input("\nEnter Stock Ticker (e.g., AAPL): ").upper().strip()
        if ticker == 'DONE':
            break
        
        if ticker not in current_prices:
            print(f"⚠️ Ticker '{ticker}' not found in mock live database. Available examples: {list(current_prices.keys())}")
            try:
                custom_price = float(input(f"Enter estimated current market price for {ticker}: "))
                current_prices[ticker] = custom_price
            except ValueError:
                print("Invalid price. Skipping entry.")
                continue

        try:
            shares = float(input(f"Enter number of shares for {ticker}: "))
            buy_price = float(input(f"Enter average purchase price per share ($): "))
        except ValueError:
            print("⚠️ Invalid numeric input for shares or price. Please try again.")
            continue

        portfolio.append({
            "ticker": ticker,
            "shares": shares,
            "buy_price": buy_price,
            "current_price": current_prices[ticker]
        })

    if not portfolio:
        print("No portfolio data entered. Exiting.")
        return

    # Calculations & Output
    filename = "portfolio_summary.csv"
    total_invested = 0
    total_current_value = 0

    print("\n" + "="*70)
    print(f"{'Ticker':<10}{'Shares':<10}{'Buy ($)':<12}{'Current ($)':<14}{'Total Val ($)':<14}{'Gain/Loss (%)':<12}")
    print("="*70)

    csv_data = []

    for item in portfolio:
        invested = item['shares'] * item['buy_price']
        market_value = item['shares'] * item['current_price']
        gain_loss_dollar = market_value - invested
        gain_loss_pct = (gain_loss_dollar / invested) * 100 if invested > 0 else 0

        total_invested += invested
        total_current_value += market_value

        print(f"{item['ticker']:<10}{item['shares']:<10.2f}{item['buy_price']:<12.2f}{item['current_price']:<14.2f}{market_value:<14.2f}{gain_loss_pct:+.2f}%")

        csv_data.append({
            "Ticker": item['ticker'],
            "Shares": item['shares'],
            "Buy Price": item['buy_price'],
            "Current Price": item['current_price'],
            "Total Invested": round(invested, 2),
            "Current Value": round(market_value, 2),
            "Gain/Loss (%)": round(gain_loss_pct, 2)
        })

    total_gain_loss_dollar = total_current_value - total_invested
    total_gain_loss_pct = (total_gain_loss_dollar / total_invested) * 100 if total_invested > 0 else 0

    print("="*70)
    print(f"Total Portfolio Value: ${total_current_value:,.2f} | Total Profit/Loss: {total_gain_loss_pct:+.2f}%")
    print("="*70)

    # Save to CSV
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ["Ticker", "Shares", "Buy Price", "Current Price", "Total Invested", "Current Value", "Gain/Loss (%)"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in csv_data:
            writer.writerow(row)

    print(f"\n📁 Successfully exported portfolio report to '{filename}'")

if __name__ == "__main__":
    track_portfolio()