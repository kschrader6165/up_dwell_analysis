import pandas as pd
import sqlite3

df = pd.read_csv("up_dwell_clean.csv", parse_dates=["week"])

conn = sqlite3.connect("up_dwell.db")
df.to_sql("dwell", conn, if_exists="replace", index=False)

print("Loaded", len(df), "rows into SQLite")

q1 = """
SELECT terminal, ROUND(AVG(dwell_hours), 1) AS avg_dwell
FROM dwell
WHERE terminal != 'System'
GROUP BY terminal
ORDER BY avg_dwell DESC
"""

q2 = """
Select terminal, week, dwell_hours
From dwell
Where terminal != 'System'
Order By dwell_hours Desc
Limit 10
"""

q3 = """
Select terminal, 
    Round(Avg(dwell_hours), 1) As avg_dwell,
    Count(*) As weeks_above_avg
From dwell
Where terminal != 'System'
And dwell_hours > (Select Avg(dwell_hours) From dwell Where terminal = 'System')
Group By terminal
Having Count(*) > 100
Order By weeks_above_avg Desc
"""

q4 = """
Select 
    Strftime('%Y', week) As year,
    Round(Avg(dwell_hours), 1) As avg_dwell
From dwell
Where terminal = 'System'
Group By year
Order By year
"""
result = pd.read_sql(q1, conn)
result2 = pd.read_sql(q2, conn)
result3 = pd.read_sql(q3, conn)
result4= pd.read_sql(q4, conn)

print("Q1: Average dwell by terminal")
print(result)

print("Q2: Worst individual weeks")
print(result2)

print("Q3: Chronically above network average")
print(result3)

print("Q4: System average dwell by year")
print(result4)

conn.close()