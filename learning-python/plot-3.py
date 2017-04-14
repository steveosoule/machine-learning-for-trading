import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("data/GE.csv")
    df[['Close', 'Adj Close']].plot()
    plt.show()  # must be called to show plots

test_run()