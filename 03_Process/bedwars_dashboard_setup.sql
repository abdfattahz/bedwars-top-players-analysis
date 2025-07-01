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

SELECT *
FROM bedwars_dashboard;

TRUNCATE TABLE bedwars_dashboard;

SELECT player, win_rate
FROM bedwars_dashboard
ORDER BY win_rate DESC
LIMIT 5;