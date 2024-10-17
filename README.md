# TURTLE TRADERS
### Video Demo: <https://youtu.be/fNIr1-9zY1s>
### Description
This code is a Python script to backtest a simplified version of the "Turtle Traders" strategy on Bitcoin using 5 years of historical price data. It uses the "Backtrader" library for backtesting, "yfinance" to get historical data, "matplotlib" and "numpy" for visualization and analysis

## The Strategy

The Turtle trading strategy is a basic trend-follwing strategy developed by Richard Dennis and William Eckhart, based on breakout signals. This script demonstrates how to implement and evaluate this strategy on Bitcoin using historical data obtained from Yahoo Finance.
for reference <https://web.archive.org/web/20080829073204/https://www.bsp-capital.com/documents/turtlerules.pdf>


## Features

- **Trading Strategy**: Implements the Turtle Trading strategy, which uses 10-day and 20-day high and low price levels to generate trading signals
- **Backtesting**: It runs a backtest to test the strategys performance on historical Bitcoin data
- **Visualization**: It provides plots of the historical data and equity curve to visualize the performance if the startegy


## Requirements

Ensure you have the following Python packages installed:

- 'numpy'
- 'matplotlib'
- 'yfinance'
- 'backtrader'

**If not you can install these using pip:**

- pip install numpy matplotlib yfinance backtrader


# Usage

## Download and run the script with:

python backtest_automation.py

## Script Details
- **Strategy Definition**: The "TurtleTraders" class defines the Turtle Trading strategy with indicators for 10-day and 20-day highs and lows
- **Backtesting Setup**: the main() function initializes the Backtrader engine(Cerebro), retrived data of Bitcoin("BTC-USD"), configures the backtesting settings and runs the backtest
- **Data and Visualization**: Historical data is fetched using yfinance, the backtestign results are plotted using backtraders plot function and the equity is plotted using matplotlib

# Code Details


## TurtTraders Class

### Indicators

#### self.day_high_20:
- is the highest price of the last 20 trading days not including today
#### self.day_low_20:
- is the lowest price of the last 20 trading days not including today
#### self.day_high_10:
- is the highest price of the last 10 trading days not including today
#### self.day_low_10:
- is the lowest price of the last 10 trading days not including today

### Trading Logic

#### Entry:
- Buy if the current price is above the 20-day high
- Buy if the current price is below the 20-day low

#### Exit:
- Close long position if the current price is below the 10-day low
- Close short position if the current price is above the 10-day high

#### Equity:
- only one trade at a time
- Stores equity values for plotting


## Main Function

### Data Acquisition
- Fetches last 5 years of historical Bitcoin data

### Backtesting Configuration:
- Sets initial cash to $100,000
- Adds the Turtle Traders strategy
- Configures risk management and commission settings

### Plotting
- Uses Backtrader to plot historical price data, signals and indicators
- Uses matplotlib to plot the equity curve showing the performance of the strategy



# Example Output
- **Backtest Plot**: Shows the Bitcoin price with buy and sell signals
- **Equity Curve**: Displays the performance of the Turtle Trading strategy over time, with the return visualized in percentage


# Notes
- You may change parameters like initial cash, commission, position size, years of data or even the strategy as needed
