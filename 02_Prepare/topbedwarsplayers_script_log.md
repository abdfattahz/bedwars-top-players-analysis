# `topbedwarsplayers.py` - Development Log

This log records the main debugging steps and changes made while building the
data extraction script for the BedWars leaderboard and player stats.

---

## Iteration overview

1. **Added debug logging**
   - First step was to add debug output to understand why the script wasn’t behaving as expected.

2. **Limit issue - only 25 players fetched**
   - Terminal output looked fine, but the script only fetched **25 players** even though `limit = 100` was set.
   - The generated CSV also contained only 25 rows.

3. **Missing stats in CSV**
   - The CSV initially contained only **player names** with no stats columns populated.
   - Added logging around the data-writing part of the script to see what was actually being passed into the CSV writer.

4. **Looping over leaderboard pages**
   - To fix the “25 players only” issue, changed the approach:
     - Previously, `limit` was defined at the top and used once.
     - Updated the script so the `get_top_usernames` function looped over the leaderboard pages internally to fetch more players.

5. **CSV overwrite issue**
   - While testing, the script crashed because the output CSV was **already open** in another program.
   - To avoid this and accidental overwrites, implemented **dynamic file naming** for CSV exports (e.g. timestamps in filenames).

6. **Improved results - 75 players fetched**
   - After adding the loop, the script was able to fetch **75 players**.
   - Even though the loop was set to run 4 times, it stopped effectively after 3 iterations, indicating a natural limit from the API/leaderboard.

7. **Loop count debugging**
   - Added extra debug logging to confirm how many times the loop actually ran.
   - Verified that the script was behaving correctly and that the leaderboard data itself stopped after a certain point.

8. **Handling server disconnects**
   - Increased `time.sleep(...)` between requests because the server was occasionally **force-closing the connection**.
   - This helped reduce rate-limit / disconnect issues.

9. **Understanding the 75-player limit**
   - Further debugging suggested that the **leaderboard itself** ends at around 75 players for the endpoint being used.
   - This explained why increasing the loop count no longer returned additional players.

10. **Hidden stats & reduced row count**
    - Even though the leaderboard contained ~75 players, some players had hidden stats.
    - These requests returned `"This Player Is Hidden From the API"`, so they were excluded.
    - Result: only **69 players** with usable stats were initially collected.

11. **Adding leaderboard placement**
    - Augmented the dataset by adding each player’s **leaderboard placement** as an explicit column.
    - This makes it easier to sort/analyze players by rank later.

12. **Refactoring to two separate CSVs**
    - Decided to split output into two different CSV files:
      - One for **leaderboard data** (rank, name, etc).
      - One for **detailed stats** (wins, losses, FKDR, bow accuracy, etc).
    - This separation made the data model clearer and easier to work with downstream.

13. **Final dataset size**
    - After accounting for hidden stats, the final BedWars stats CSV contains **68 players**.
    - The difference between 75 leaderboard entries and 68 stats rows is explained by players whose stats are hidden from the API.

---

## Summary

- Started with a simple script that only fetched 25 players with names only.
- Iteratively:
  - added logging,
  - fixed pagination/looping,
  - handled file overwrites with dynamic filenames,
  - dealt with API limits and server disconnects
  - and cleaned up hidden-stat cases.
- Final result: two CSVs (leaderboard + stats) covering 68 top BedWars players with usable stats.
