import requests

url = "https://api-web.nhle.com/v1/score/now"
response = requests.get(url)
data = response.json()

games = data.get("games", [])

print(f"--- NHL Games ({data.get('currentDate', 'Today')}) ---")

for game in games:
    away_team = game.get("awayTeam", {}).get("name", {}).get("default", "Away")
    away_score = game.get("awayTeam", {}).get("score", 0)

    home_team = game.get("homeTeam", {}).get("name", {}).get("default", "Home")
    home_score = game.get("homeTeam", {}).get("score", 0)

    game_state = game.get("gameState", "N/A")  # e.g., 'FUT' (Future), 'OFF' (Final), 'LIVE'

    print(f"{away_team:<20} {away_score} @ {home_score} {home_team:<20} | Status: {game_state}")