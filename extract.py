import pandas as pd

df = pd.read_excel("EP724 Consolidated Data through 2026-10-07.xlsx")

rr_col = df.columns[0]
cat_col = df.columns[1]

up_dwell = df[(df[rr_col] == "UP") & (df[cat_col] == 2)].copy()
print(len(up_dwell))
print(df[rr_col].str.strip().unique())
id_cols = [rr_col, cat_col, df.columns[3], df.columns[4]]
date_cols = [c for c in df.columns if isinstance(c, pd.Timestamp) or hasattr(c, 'year')]
print(type(df.columns[6]), df.columns[6])
long = up_dwell[id_cols + date_cols].melt(
    id_vars=id_cols,
    value_vars=date_cols,
    var_name="week",
    value_name="dwell_hours"
)

long["week"] = pd.to_datetime(long["week"])
long = long.rename(columns={df.columns[4]: "terminal"})
long = long[["week", "terminal", "dwell_hours"]]
long = long.sort_values(["terminal", "week"]).reset_index(drop=True)

long.to_csv("up_dwell.csv", index=False)

