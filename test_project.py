from project import load_data, set_up_cerebro, plot_strategy
import backtrader as bt
import numpy as np
from unittest.mock import patch, MagicMock

#see if this function returns data correctly of "BTC-USD"
def test_load_data():
    asset = "BTC-USD"

    #check if load_data returns a data frame
    data = load_data(asset)

    #check if there is data
    assert not data.empty

    #check if data is in the right format
    assert all(column in data.columns for column in ["Open", "High", "Low", "Close"])




def test_set_up_cerebro():
    #create test data
    test_data = MagicMock()

    #call cerebro with test data
    cerebro = set_up_cerebro(test_data)

    #check if cerebro which is used is an instance of the cerebro from backtrader
    assert isinstance(cerebro, bt.Cerebro)

    #test for how much cash there is
    assert cerebro.broker.get_cash() == 100000

    #check if data is correctly added to cerebro
    assert len(cerebro.datas) > 0




@patch("matplotlib.pyplot.show")
def test_plot_strategy(test_show):
    #Create a test strategy result
    test_strategy = MagicMock()
    test_strategy.equity = [100000, 101000, 102000]
    test_results = [test_strategy]

    #Create test historical data
    test_history = MagicMock()
    test_history.index = np.array(["2024-09-01", "2024-09-02", "2024-09-03"], dtype="datetime64")

    #Call the plot_startegy function
    cerebro = MagicMock()
    plot_strategy(cerebro, test_results, test_history, "BTC-USD")

    #test if plt.show() is called
    test_show.assert_called_once()
