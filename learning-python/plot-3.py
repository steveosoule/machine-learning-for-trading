"""Plot High prices for IBM"""

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/AAPL.csv")
    df[['Close', 'Adj Close']].plot()
    plt.show()  # must be called to show plots