import requests
import pandas as pd
import time

from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M")

# --- CONFIG ---
STAT = 'wins'
INTERVAL = 'total'
MODE = 'ALL_MODES'
#LEADERBOARD_URL = f'https://stats.pika-network.net/api/leaderboards?type=bedwars&stat={STAT}&interval={INTERVAL}&mode={MODE}&offset=0'
PROFILE_URL_BASE = 'https://stats.pika-network.net/api/profile/'

# --- Step 1: Get top 100 usernames from leaderboard ---
def get_top_players(limit=100):
    players = []
    for offset in range(0, limit, 25):
        url = f"https://stats.pika-network.net/api/leaderboards?type=bedwars&stat=wins&interval=total&mode=ALL_MODES&offset={offset}&limit=25"
        response = requests.get(url)
    
        try:
            data = response.json()
            if 'entries' not in data or not data['entries']:
                print(f"⚠️ Offset {offset}: No entries found - likely end of leaderboard.")
                break

            batch = [{
                'Player': entry['id'],
                'Placement': entry['place'],
                'Clan' : entry.get('clan', '') #this is to handle players that dont have clan
                } for entry in data['entries']]
            
            print(f"🔎 Offset {offset}: Retrieved {len(batch)} usernames with placement")
            players.extend(batch)

            # break early if fewer than 25 returned
            if len(batch) < 25:
                print(f"⚠️ Offset {offset}: Fewer than 25 usernames returned - stopping pagination.")
                break

        except Exception as e:
            print(f"❌ Failed to parse leaderboard at offset {offset}: {e}")

    print(f"✅ Retrieved {len(players)} usernames from leaderboard.")
    return players

# --- Step 2: Fetch detailed stats per player ---
def get_player_stats(player_info):
    username = player_info['Player']
    placement = player_info['Placement']

    url = f"{PROFILE_URL_BASE}{username}/leaderboard?type=bedwars&interval={INTERVAL}&mode={MODE}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"❌ Failed to fetch {username} (status: {response.status_code})")
        return None

    try:
        # print(f"📄 Raw response for {username}: {response.text}") # for debugging purposes only
        stats_json = response.json()
        stats = {'Player': username}

        for stat_name, stat_data in stats_json.items():
            if stat_data["entries"] and len(stat_data["entries"]) > 0:
                stats[stat_name] = int(stat_data["entries"][0]["value"])
            else:
                stats[stat_name] = 0  # for missing/null entries

        print(f"✅ Collected stats for {username} (Placement #{placement})")
        return stats
    
    except Exception as e:
        print(f"❌ Error parsing response for {username}: {e}")
        return None

# --- Main script ---
top_players = get_top_players()

# --- Save leaderboard stats to seperate CSV ---
leaderboard_df = pd.DataFrame(top_players)
leaderboard_df.to_csv(f"leaderboard_{timestamp}.csv", index=False)
print("📄 Saved leaderboard stats to leaderboard.csv")

all_stats = []
for player in top_players:
    print(f"📦 Fetching stats for {player['Player']}...")
    player_stats = get_player_stats(player)
    if player_stats:
        all_stats.append(player_stats)
    time.sleep(1.5)  # Rate limit friendly (so that the we are not getting flagged by the api)

# --- Save to CSV ---
df = pd.DataFrame(all_stats)

# Reorder columns if they exist
preferred_cols = ['Player', 'Games played', 'Wins', 'Losses', 'Highest winstreak reached', 'Kills', 'Deaths', 'Final kills', 'Final deaths', 'Beds destroyed', 'Melee kills', 'Bow kills', 'Void kills', 'Arrows shot', 'Arrows hit']
ordered_cols = [col for col in preferred_cols if col in df.columns]
df = df[ordered_cols]

# --- Preview before saving --- (debugging purposes only)
# print("📊 Final DataFrame preview:")
# print(df.head())
# print("🧮 Columns:", df.columns.tolist())

# --- Dynamic naming to avoid overwrite issue ---
df.to_csv(f'top_100_bedwars_stats_{timestamp}.csv', index=False)
print("✅ Saved Top 100 Bedwars Players Stats to top_100_bedwars_stats.csv")