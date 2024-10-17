#import all libraries needed
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import backtrader as bt



#define a trading strategy
class TurtleTraders(bt.Strategy):
    def __init__(self):
        #defining the Indicators
        self.day_high_20 = bt.ind.Highest(self.data.high, period=20)
        self.day_low_20 = bt.ind.Lowest(self.data.low, period=20)
        self.day_high_10 = bt.ind.Highest(self.data.high, period=10)
        self.day_low_10 = bt.ind.Lowest(self.data.low, period=10)
        self.equity = list() #List to store the equity values


    #defining the trading logic and buy and sell signals
    def next(self):
        day_high_20 = self.day_high_20[-1]
        day_low_20 = self.day_low_20[-1]
        day_high_10 = self.day_high_10[-1]
        day_low_10 = self.day_low_10[-1]

        current_price = self.data[0]

        if not self.position: #check if there is already a position
            if current_price > day_high_20: #if price is above the 20-day high
                self.buy() #go long

            if current_price < day_low_20:  # if price is below the 20-day low
                self.sell()  # go short


        else: #if there  is no position
            if self.position.size > 0: #if in a long
                if current_price < day_low_10: #if price is below 10-day low
                    self.close() #close the long

            if self.position.size < 0: #if in a short
                if current_price > day_high_10: #if price is above the 10-day high
                    self.close() #close the short position

        #Equity value for plotting results
        self.equity.append(self.broker.get_value())

def load_data(asset, period="5y", interval="1d"):
    # Get BTC chart
    btc = yf.Ticker(asset)

    # BTC historical data
    history = btc.history(period="5y", interval="1d")

    # Return the historical data
    return history

def set_up_cerebro(data):
    # creating a cerebro instance
    cerebro = bt.Cerebro()

    # set the cash value to 100,000
    cash = 100000
    cerebro.broker.set_cash(cash)

    # add the strategy
    cerebro.addstrategy(TurtleTraders)

    # sort the data
    feed = bt.feeds.PandasData(dataname=data)

    # add data to cerebro
    cerebro.adddata(feed)

    # add risk
    cerebro.addsizer(bt.sizers.PercentSizer, percents=1)

    # add commission of 0.5%
    cerebro.broker.setcommission(commission=0.005)

    return cerebro


def plot_strategy(cerebro, results, history, asset):
    # Plot the data
    cerebro.plot(volume=False, style='candles', barup='green', bardown='black', grid=False)

    # plot the results of the strategy
    strategy = results[0]
    equity = np.array(strategy.equity)
    dates = history.index[:len(equity)]

    plt.figure(figsize=(12, 6))
    plt.plot(dates, (equity - 100000) / 1000, label='Equity', color='green')
    plt.xlabel(f"Date")
    plt.yticks(np.arange(-1, 10, 0.5))
    plt.ylabel(f"Results of the Turtle Strategy on {asset} in percent")
    plt.grid(True)
    plt.title(f"Turtle Strategy performance")
    plt.legend(["Return over time"])
    plt.show()


def main():

    asset = "TSLA"

    #call the load data function
    data = load_data(asset)

    #call the set up cerebro function
    cerebro = set_up_cerebro(data)

    #Run the backtest
    results = cerebro.run()

    #call the plot strategy function
    plot_strategy(cerebro, results, data, asset)



if __name__ == "__main__":
    main()
