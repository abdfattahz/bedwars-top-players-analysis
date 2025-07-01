1. create a schema for this 
2. creating the table for data from google sheet
3. downloading the google sheet "dashboard" as csv
4. imported the data to mySQL using table data import wizard (gui)
5. realise that there is some typo in the table created. 
6. delete table using drop table function
7. did the ORDER BY win_rate and limit it to 5 to see the top 5 win rate but realised there's something wrong with the data. there's actually several players with higher win rate but it doesnt show up. 
8. trying to investigate. currently using SELECT COUNT to find if the row is imported correctly and tally with the google sheet. 
9. found that there are only 44 rows. so there might me some error during import. 
10. tried running the query to find the actual no 1 player inside the table. the result shows the player is not inside the table. 
11. try checking if there's NULL data inside the table. and also double checking all the types for each column
12. after further investigation, i realised that inside the csv file (after oopening it using text editor) there's actually a wrong format under melee/ranged kill ratio. there's somehow a quote ("") for some data. 
13. When you set the format to “Number” (e.g. 1,000.12), Google Sheets adds commas as thousands separators

When you export to .csv, Google Sheets tries to preserve those commas by wrapping the whole value in quotes (e.g. "2,271.63")

MySQL sees that comma as a column separator, not a thousands marker — so it misreads the row, and skips it
14. so what i did is i go to google sheet, i created a new spreadsheet and copy all the value from the dashboard and pasted the value only on the new spreadsheet named cleaneddashboard then what i did is, i select all the table column (that has numbers) and change it to custom number format 0.00 to make it consistent.
14. so after doing the fix with the google sheet, i downloaded it back in csv
15. now i need to remove all the data from the current table to replace with a fixed one. so i use TRUNCATE TABLE to remove all the rows data without messing with the table structure.
16. then i imported back the new csv file to the table. 
17. did the Top 10 Players by Win Rate query
18. did the Top 10 Accuracy vs Final/KD. realise that the bow accuracy doesnt really increase their final kdr. 
19. try to dive deeper in this data. did the query to identify top 10 players win rate. realise that the top 10 players are all invested to  melee ranged combat styles. even if we didnt limit it to 10, all top 100 players are all combat styles. when we dive deeper, we found out that this is because the bow is quite an expensive item inside the shop. plus the resource generator is quite slow. 