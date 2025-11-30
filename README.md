# BedWars Top Players - Data Pipeline & Analysis (WIP)

This project is a **data pipeline + analysis case study** based on Minecraft BedWars stats from the Pika Network (one of the largest free Minecraft server)

I used it to practice the full analytics workflow:

> **API → Python → CSV → Sheets/Excel → MySQL → SQL queries → (future) dashboard**

and to answer a very practical question for myself:

> *“If I want to get good at BedWars, what do top players actually look like in the data?”*

## What this project demonstrates

**Data Analytics skills**

- Framing fuzzy questions into measurable metrics using the Google Data Analytics framework (**Ask → Prepare → Process → Analyze → Share → Act**)
- Designing metrics: win rate, K/D, FKDR, bow accuracy, kill-type ratios, melee/ranged ratios
- Cleaning and transforming data in **Google Sheets / Excel**:
  - VLOOKUP / INDEX-MATCH  
  - IF logic for missing values  
  - percentage vs decimal formats
- Writing **SQL** to:
  - rank players (Top N by metric)
  - compare metrics (e.g. bow accuracy vs FKDR)
  - check data quality (row counts, NULL checks)

**Data Engineering skills**

- **Python** data extraction script (`topbedwarsplayers.py`):
  - Consuming a REST API
  - Pagination over leaderboard pages
  - Handling hidden stats / error responses
  - Simple rate limiting with `time.sleep`
  - Dynamic filenames to avoid CSV overwrite
- Building a small **data pipeline**:
  - Raw API → CSV → spreadsheet → cleaned CSV → MySQL table
- Designing & adjusting a **database schema** (`bedwars_dashboard_schema.sql`)
- Debugging **CSV import** issues in MySQL:
  - Thousands separators and quoted numbers
  - Misaligned columns
  - Using `TRUNCATE` + re-import to fix bad loads
- Keeping **work logs** for reproducibility and storytelling

---

## Tech Stack

- **Language:** Python
- **Data collection:** Pika Network public stats API
- **Data storage & cleaning:** Google Sheets / Excel → CSV
- **Database:** MySQL
- **Querying:** SQL (`bw_analysis.sql`, `bedwars_dashboard_schema.sql`)
- **Version control:** Git + GitHub
- **Documentation:** Markdown logs in each phase

---

## Repository structure

This repo follows the Google Data Analytics course structure:

```text
01_Ask/       # project idea, questions and data plan
02_Prepare/   # Python script, raw API exports, script dev log
03_Process/   # Sheets transformations, cleaned CSV, MySQL logs & SQL, query screenshots
04_Analyze/   # (planned) final dashboard + story
05_Share/     # (planned)
06_Act/       # (planned)
````

Key files:

* `01_Ask/project_brief.md`
  High-level motivation and scope

* `01_Ask/analysis_questions.md`
  Draft analysis questions and personal goals

* `01_Ask/data_sources.md`
  Plan for API → Sheets → MySQL data flow

* `02_Prepare/topbedwarsplayers.py`
  Python script to:

  * fetch top leaderboard players
  * fetch detailed stats for each
  * handle pagination, hidden stats and rate limiting
  * save separate CSVs for leaderboard and stats

* `02_Prepare/topbedwarsplayers_script_log.md`
  Step-by-step dev log (what broke, how it was fixed)

* `03_Process/BW Case Study - Dashboard.csv`
  Initial dashboard export from Sheets (raw-ish)

* `03_Process/BW Case Study - CleanedDashboard.csv`
  Cleaned version used for MySQL import

* `03_Process/sheets_transformation_log.md`
  How metrics were calculated and formatted in Sheets/Excel

* `03_Process/mysql_import_log.md`
  Detailed log of the MySQL import, issues and fixes

* `03_Process/bedwars_dashboard_schema.sql`
  Table schema + basic sanity queries

* `03_Process/bw_analysis.sql`
  Main analysis queries (top N players, bow accuracy vs FKDR, playstyle exploration, etc)

* `03_Process/query_*.png`
  Screenshots of SQL query results (top 5/10 winrate, bow accuracy vs FKDR, combat style)

---

## Data flow / pipeline

1. **Ask**

   * Define the goal: understand what top BedWars players look like and how I can learn from them
   * Draft analysis questions in `01_Ask/`

2. **Prepare (Python + API)**

   * Use `topbedwarsplayers.py` to:

     * Fetch leaderboard players
     * Fetch detailed stats for each player
     * Handle players whose stats are hidden (`"This Player Is Hidden From the API"`)
     * Save:

       * `leaderboard_*.csv`
       * `top_100_bedwars_stats_*.csv`

3. **Process (Sheets + MySQL)**

   * Load CSVs into **Google Sheets / Excel**:

     * Create calculated metrics (win rate, K/D, FKDR, bow accuracy)
     * Handle missing clan names and unclassified kills
     * Export a clean, numeric-only CSV (`CleanedDashboard`)
   * Import cleaned CSV into **MySQL**:

     * Fix CSV formatting issues (thousands separators, quoted decimals)
     * Use `TRUNCATE` + re-import to correct bad loads
     * Run analysis queries and export screenshots

4. **Analyze / Share / Act (planned)**

   * Build a clearer dashboard (likely in Sheets or a BI tool)
   * Summarise insights and practical tips for “how to play better”
   * Turn this into a portfolio-style write-up

---

## How to run parts of this project

> This project is mainly a **case study**, but parts of it are reproducible
> API behaviour and leaderboard contents may have changed since this snapshot

### 1. Run the Python extraction script

Requirements (rough):

* Python 3.x
* `requests`
* `pandas` (optional, depending on your version of the script)

Basic idea:

```bash
cd 02_Prepare
python topbedwarsplayers.py
```

The script will:

* call the Pika Network stats API
* fetch leaderboard + player stats (up to the API’s limits)
* write CSV files with timestamps in their names

> Note: you may need to adjust base URLs or parameters if the API changed

### 2. Use the SQL scripts

* Create a MySQL schema
* Import `BW Case Study - CleanedDashboard.csv` into a table matching `bedwars_dashboard_schema.sql`
* Run queries from `bw_analysis.sql` to reproduce the Top 5 / Top 10 lists and comparisons

---

## Project status

* ✅ **01_Ask** - initial planning and data source design
* ✅ **02_Prepare** - Python extraction and CSV exports
* ✅ **03_Process** - cleaning, MySQL import, initial queries & screenshots
* 🔄 **04_Analyze** - building a clearer, presentation-ready dashboard
* 🔜 **05_Share / 06_Act** - final storytelling and recommendations

---

## Why this is relevant for data roles

Even though the dataset is from a game, the skills are directly transferable:

* **Data Analyst:**
  Framing questions, designing metrics, cleaning and combining datasets, writing SQL and explaining data quality decisions

* **Data Engineer / Analytics Engineer:**
  Building a small pipeline end-to-end, dealing with real-world API/CSV quirks, defining schemas and making the data reliable enough for downstream analysis

If you’re reviewing this as a recruiter or hiring manager and want a quick walkthrough, feel free to start at:

* `01_Ask/project_brief.md` - for context, then
* `03_Process/mysql_import_log.md` - to see how I debugged real data issues, then
* `03_Process/bw_analysis.sql` + `query_*.png` - to see the analysis outputs

---

## 📬 Contact

If you’d like to chat about this project or similar work:

* Linkedin: [[linkedin.com/abdulfattah](https://www.linkedin.com/in/abdfattah/)]

Let's connect!
