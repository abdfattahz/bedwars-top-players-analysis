# Data Sources - Plan (Draft)

This is the plan for where I expect the data to come from and how I’ll move it around.  

## 1. Game stats API

- Target: Pika Network BedWars stats API.
- Plan:
  - Use a small Python script to:
    - grab the **leaderboard** (top players),
    - loop through those players and pull their detailed stats.
- Things to check:
  - exact API endpoints and parameters,
  - whether there are rate limits,
  - whether some players can hide their stats,
  - how many players I can realistically collect.

## 2. Sheets / Excel

- After getting the raw JSON/CSV from the API:
  - Load it into Google Sheets or Excel.
  - Use formulas to:
    - calculate win rate, K/D, FKDR,
    - calculate bow accuracy,
    - compute percentages for melee / bow / void kills.
- I’ll probably export a cleaner CSV from here for SQL.

## 3. SQL database

- Import the cleaned CSV into MySQL.
- Use SQL to:
  - run ranking queries (top 10 by X metric),
  - join or re-calculate any metrics I need,
  - prepare outputs for charts.

## Open questions / risks

- Will the API give me enough players?
- Will all the stats I want (bow accuracy, kill types, etc.) actually be available?
- Will formatting from Sheets to CSV to MySQL cause problems?