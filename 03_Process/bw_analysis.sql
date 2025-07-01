-- Step 1: Create schema
CREATE DATABASE bw_analysis;

-- Step 2: Use schema
USE bw_analysis;

-- Step 3: Create table
CREATE TABLE bedwars_dashboard (
	palcement INT,
    player VARCHAR(50),
    clan VARCHAR(50),
    win_rate FLOAT,
    kd_ratio FLOAT,
    final_kd_ratio FLOAT,
    bow_accuracy FLOAT,
    beds_per_win FLOAT,
    melee_ranged_ratio FLOAT
);

-- Step 4: View table
SELECT *
FROM bedwars_dashboard;

-- Step 5: Realise there's some typing error, Delete the table
DROP TABLE bedwars_dashboard;

-- Step 6: Recreate the correct table
CREATE TABLE bedwars_dashboard (
	placement INT,
	player VARCHAR(50),
	clan VARCHAR(50),
	win_rate FLOAT,
	kd_ratio FLOAT,
	final_kd_ratio FLOAT,
	bow_accuracy FLOAT,
	beds_per_win FLOAT,
	melee_ranged_ratio FLOAT
);

-- Step 7: Insightful queries
SELECT player, win_rate
FROM bedwars_dashboard
ORDER BY win_rate DESC
LIMIT 5;

-- Step 8: Realised some error with the data, trying to debug
SELECT COUNT(*) 
FROM bedwars_dashboard;

-- finding the missing player
SELECT *
FROM bedwars_dashboard
WHERE player = 'Mrays';
    
-- checking for NULL or wrong types
SELECT player
FROM bedwars_dashboard
WHERE win_rate IS NULL;
    
DESCRIBE bedwars_dashboard;

-- delete the current table and replace it with the fixed one
TRUNCATE TABLE bedwars_dashboard;

-- Top 10 Players by Win Rate
SELECT player, win_rate
FROM bedwars_dashboard
ORDER BY win_rate DESC
LIMIT 10;

-- Top 10 Accuracy vs Final/KD
SELECT player, bow_accuracy, final_kd_ratio
FROM bedwars_dashboard
ORDER BY bow_accuracy DESC
LIMIT 10;

-- Classifying top players playstyles
SELECT player,
		CASE 
			WHEN melee_ranged_ratio > 2 THEN 'Melee-heavy'
			WHEN melee_ranged_ratio < 0.5 THEN 'Ranged-heavy'
			ELSE 'Balanced'
		END AS combat_style,
        kd_ratio,
        win_rate
FROM bedwars_dashboard
ORDER BY win_rate DESC;

-- Flag Elite players
SELECT player, win_rate,
		CASE 
			WHEN win_rate > 0.75 THEN 'Elite'
			ELSE 'Standard'
		END AS is_elite
FROM bedwars_dashboard;




    
    