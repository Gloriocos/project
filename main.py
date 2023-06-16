import pandas as pd

songs_df=pd.read_csv("songs-of-10s.csv")
#head() prints the first 5 rows
print(songs_df.head())
print(songs_df.columns)
