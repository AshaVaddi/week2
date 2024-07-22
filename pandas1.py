import pandas as pd
from io import StringIO


csv_data = """name,age,city
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago
"""


csv_file = StringIO(csv_data)
df = pd.read_csv(csv_file)
print(df)
