import pandas as pd
import sqlite3

conn = sqlite3.connect("up_rail.db")

dwell = pd.read_csv("up_dwell_clean.csv")
network = pd.read_csv("up_network_clean.csv")

dwell.to_sql("dwell", conn, if_exists = "replace", index = False)
network.to_sql("network", conn, if_exists = "replace", index = False)

print("Loaded", len(dwell) + len(network), "Rows into SQLite")

conn.close()