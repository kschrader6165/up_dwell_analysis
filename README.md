# UP Terminal Dwell Analysis

Analyzed Union Pacific's public terminal dwell data (STB EP724, 2017–2026) 
to identify bottlenecks and service trends.

**Data source:** Surface Transportation Board EP724 consolidated weekly filings  
**Tools:** Python, pandas, SQLite  
**Rows analyzed:** 5,479 (498 weeks × 11 terminals)

## Key Findings

- West Colton CA and Pine Bluff AR are UP's highest-dwell terminals (27–28 hrs avg)
- System-wide dwell peaked in 2017–2018 (~30 hrs) and has improved to ~20 hrs in 2026
- Houston spiked to 75.8 hrs in Sept 2017 (Hurricane Harvey)
- Pine Bluff was above the network average for 352 of 498 weeks — chronically slow

## Files

- `extract.py` — reads STB xlsx, filters UP terminal dwell rows, outputs long-format CSV
- `clean.py` — converts types, drops nulls, saves clean CSV
- `queries.py` — loads SQLite, runs 4 analytical queries
- `up_dwell_clean.csv` — cleaned dataset

## 30-Second Pitch

Union Pacific files weekly terminal dwell data with federal regulators. I pulled 
nine years of that data, cleaned it in pandas, and queried it in SQLite to find 
which terminals are the biggest bottlenecks and whether service is improving. 
Dwell time matters for Loup because late terminal processing means late deliveries.