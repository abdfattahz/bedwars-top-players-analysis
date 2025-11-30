# Google Sheets Processing Log

1. Imported the stats collected from the Python script into a sheet named **BW Case Study**.
2. Imported leaderboard stats into the **Leaderboard** sheet.
3. Imported individual player stats into the **PlayerStats** sheet.
4. Used **VLOOKUP** to merge leaderboard placement with player names.
5. Added clan information using another **VLOOKUP**.
6. Realised that if a player had no clan, the VLOOKUP returned a blank value.
7. Switched to an **IF** function so players without a clan would display **N/A** instead of a blank cell.
8. Used **INDEX/MATCH** to compute the following derived metrics:
   - win rate  
   - K/D  
   - FKDR  
   - bow accuracy  
   - beds per win
9. The initial calculations showed too many decimal places, so I changed the formats to **percentages** for easier reading.
10. Win rate formula:
    - `total attempts = wins + losses`  
    - `win rate = wins / total attempts`
11. Changed the **K/D** cell format to “Number (2 decimal places)”:
    - `K/D = kills / deaths`
12. Defined **FKDR** as:
    - `FKDR = final_kills / final_deaths`
13. Updated FKDR format to “Number (2 decimal places)” for consistency.
14. Changed **bow accuracy** to a percentage format for readability:
    - `bow accuracy = arrows_hit / arrows_shot`
15. Not all kill types were clearly represented in the dataset, so I created an **unclassified kills** field in `PlayerStats`.  
    This includes:
    - kills using items under “Other” or “Rotational” categories in the shop (e.g., golem, fireballs)  
    - weapon kills only track sword and punch kills
16. Added a **melee/ranged ratio** metric.
17. Planned to compute kill-type percentages later:
    - `% Melee = MeleeKills / TotalKills`  
    - `% Bow = BowKills / TotalKills`  
    - `% Void = VoidKills / TotalKills`
18. Converted all percentage fields back to **decimal values** to make formats consistent and to ensure smooth import into MySQL.
