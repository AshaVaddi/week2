import pandas as pd

data = [10, 20, 30, 40, 50]
index = ['A', 'B', 'C', 'D', 'E']

series = pd.Series(data, index=index)

print(series)
