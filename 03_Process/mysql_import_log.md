# MySQL Processing Log

1. Created a schema for the project.
2. Created the table for data imported from Google Sheets.
3. Downloaded the Google Sheet “Dashboard” as a CSV file.
4. Imported the CSV into MySQL using the Table Data Import Wizard (GUI).
5. Realised there was a typo in the table structure I created.
6. Dropped the table using `DROP TABLE` and recreated it correctly.
7. Ran an `ORDER BY win_rate` query (LIMIT 5) to view the top 5 players.  
   Noticed something was wrong — some players with higher win rates were missing.
8. Started investigating by using `SELECT COUNT(*)` to check if the number of imported rows matched the sheet.
9. Found that only **44 rows** were imported, which was fewer than expected → import issue suspected.
10. Ran a query to find the actual #1 win-rate player from the sheet.  
    The result showed the player **was not in the table** at all.
11. Checked for `NULL` values and double-checked the data types for each column.
12. Opened the CSV in a text editor and found formatting issues in the melee/ranged kill ratio column.  
    Some numeric fields were wrapped in quotes.
13. Root cause:
    - Google Sheets formats large numbers with commas (e.g., `1,000.12`).
    - When exporting to CSV, Sheets wraps these values in quotes (e.g., `"2,271.63"`).
    - MySQL interprets commas as column separators → causing misaligned or skipped rows.
14. Fix:
    - Created a new spreadsheet for cleaning.
    - Copied all values from the original dashboard into a **CleanedDashboard** sheet.
    - Set all numeric columns to **Custom number format: `0.00`** for consistency.
15. Exported the cleaned sheet as a new CSV.
16. Used `TRUNCATE TABLE` to clear existing data while keeping the table structure.
17. Reimported the cleaned CSV into MySQL.
18. Ran the **Top 10 Players by Win Rate** query successfully.
19. Ran a **Top 10 Bow Accuracy vs Final K/D** query and noticed bow accuracy did not significantly increase final K/D.
20. Looked deeper:
    - The top 10 win-rate players mainly relied on melee/ranged combat.
    - Even beyond the top 10, most top 100 players were still melee-focused.
    - Likely due to bow being expensive in the shop and the generator being slow, making bow usage less common.
