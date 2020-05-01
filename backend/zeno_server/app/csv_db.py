import pandas as pd

data = pd.read_csv('../media/task_data.csv')
df = pd.DataFrame(data, columns=['id', 'timestamp', 'temperature', 'duration'])

for row in df.itertuples():
    print(row)