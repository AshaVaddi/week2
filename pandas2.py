import pandas as pd


df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})


max_value = df['B'].max()


print("Maximum value in column 'B':")
print(max_value)
