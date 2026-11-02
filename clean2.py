import pandas as pd

df = pd.read_csv("ep724-public-data.csv", parse_dates=["report_period_start_date"])

measures = [
    "average_terminal_dwell_time",
    "average_train_speed",
    "average_cars_on_line",
    "average_trains_holding_crew",
    "average_trains_holding_locomotive",
    "average_trains_holding_other",
    "average_trains_holding_total"
]
df = df[df["measure_name_analytics"].isin(measures)]

#print(df.columns.tolist())

df = df[["measure_name_analytics", "sub_measure_analytics", "fact_value", "report_year", "report_period_start_date", "measure_units"]]

df = df.dropna(subset=["fact_value"])

df.to_csv("up_network_clean.csv", index=False)

#print(len(df))

#print(df["measure_name_analytics"].value_counts())