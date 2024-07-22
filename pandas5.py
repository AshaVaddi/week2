import pandas as pd
from io import StringIO


csv_data = """A,B,C
1,6,11
2,7,12
3,8,13
4,9,14
5,10,15
"""


csv_file = StringIO(csv_data)


df = pd.read_csv(csv_file)


first_ten_rows = df.head(10)


print(first_ten_rows)
