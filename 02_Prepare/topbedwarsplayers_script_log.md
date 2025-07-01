1. add a debug to know why it didnt work
2. output in the terminal looks fine. only prob is that it shows fetched 25 players only instead of limit 100 that i put inside the script
3. the csv file created also shows only 25 players and no stats. only names.
4. for the 25 players only fetched i decided to make a loop. 
previously limit define on top. but now doing limit loop inside the get_top_usernames block
5. for only names showing inside csv. i add logging first
6. tried running the latest script but encountered error. turns out it because i have my previous created csv opened so now i put in a script for a dynamic naming. to avoid overwriting issue
7. managed to get 75 players this time. eevntho made the loop for 4 times, it still stops at 3 times. 
8. adding a debug script to know how many times it loops
9. increased the time.sleep because the server force close
10. tried debugging the limit to know why it only stops at third loop. seems like the leaderboard ends at 75. 
11. still getting fewer than 75 because some players hide their stats. so only managed to fetch 69 data for the stats.
12. added leaderboard placement.
13. decided to redo the script and make it save leaderboard api and stats api in two different csv  file
14. only able to retrieve 68 players for the bedwars stats since some player's stats are hidden from the api "This Player Is Hidden From the API"