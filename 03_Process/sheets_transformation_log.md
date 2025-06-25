1. importing stats collected from the script to sheet named BW Case Study
2. the leaderboard stats is imported under the Leaderboard sheet
3. the player's stats imported under the PlayerStats sheet. 
4. using vlookup to merge placement with players name
5. using vlookup to add clan in it too
6. relise that if i use the same function as the placement, if the player didnt join any clan, it will leave blank column.
7. decided to use IF function so that if the player did not join any clan it will fill the column with N/A instead
8. decided to use INDEX/MATCH for win rate kdr, fkdr, bow accuracy and beds per win
9. the calculation gave too many decimal point. i change it to % for easier analysis
10. the formula for winrate is, 
win = wins / total attempt
total attempt = wins + losses
11. changed K/D format to numbers so it displays 2 decimal point only
K/D = Kills / Death
12. FKDR = Final kills / Final Death
13. changed the FKDR format to numbers so that it will only display 2 decimal point
14.  changed the bow accuracy to % for easier analysis
bow accuracy = arrow shot / arrow hit
15. not all kills are presented inside this data. so i decided to put unclassified kills into the playerstats sheet.
this includes : player kills using items under others or rotational category in the shop eg. golem, fireballs, other weapons (only track swords and punch's kills), etc
16. added melee/ranged ratio
17. need to compute the percentage of each kill type later
% Melee = MeleeKills / TotalKills
% Bow = BowKills / TotalKills
% Void = VoidKills / TotalKills
18. change all the % to decimal to make everything consistent. and easy to transfer the data to mySQL
