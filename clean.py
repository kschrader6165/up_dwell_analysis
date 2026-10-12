import pandas as pd

df = pd.read_csv("up_dwell.csv", parse_dates=["week"])

print(df.dtypes)
print(df.isnull().sum())
print(df["dwell_hours"].describe())
print(df["terminal"].unique())

df["dwell_hours"] = pd.to_numeric(df["dwell_hours"], errors="coerce")

df = df.dropna(subset=["dwell_hours"])

print(df.dtypes)
print(df.isnull().sum())
print(df["dwell_hours"].describe())
print(df.shape)

df.to_csv("up_dwell_clean.csv", index=False)