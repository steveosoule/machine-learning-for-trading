import pandas as pd
import matplotlib.pyplot as plt

def test_run():
	df = pd.read_csv('data/GLD.csv')
	df = df.sort(['Date'], ascending=[True])
	df.plot()
	plt.show()

test_run()