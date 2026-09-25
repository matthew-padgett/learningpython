import argparse
from nhlpy import NHLClient
from datetime import datetime, timedelta

client = NHLClient(
    debug=True,
    timeout=30,
    ssl_verify=True,
    follow_redirects=True
)

def get_games(date=None, show_broadcast=False):
    current_date = datetime.today().strftime("%Y-%m-%d")
    tomorrow_date = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    if date is None:
        date = current_date

    games = client.schedule.daily_schedule(date=f"{date}")

    game_list = games.get('games', [])
    if not game_list:
        print(f"No games found for {date}")

    for game in games.get('games', []):
        away_team = game['awayTeam']['commonName']['default']
        home_team = game['homeTeam']['commonName']['default']

        game_time = datetime.fromisoformat((game['startTimeUTC']).replace("Z,", "+00:00"))
        local_game_time = game_time.astimezone().strftime("%I:%M %p")

        game_state = game['gameState']
        if game_state == "LIVE":
            local_game_time = "LIVE"
        elif date == tomorrow_date:
            local_game_time = f"| Tomorrow {local_game_time}"
        elif date != current_date:
            formatted_date = datetime.strptime(date, "%Y-%m-%d")
            local_game_time = formatted_date.strftime("%a, %b %d" + f" {local_game_time}")
        else:
            local_game_time = local_game_time

        output =  f"{away_team} @ {home_team} {local_game_time}"

        if show_broadcast:
            broadcast = game.get('tvBroadcasts', [])
            networks = [b['network'] for b in broadcast if 'network' in b]
            broadcasts = ", ".join(networks)
            broadcast_list = f"on {broadcasts}" if networks else "No networks listed."
            output += f"{broadcast_list}"

        print(output)

parser = argparse.ArgumentParser(
    description="NHL CLI"
)

parser.add_argument(
    "--today",
    action="store_true",
    help="Fetch today's NHL games."
)

parser.add_argument(
    "--date",
    type=str,
    help="Fetch NHL games from a specific date."
)

parser.add_argument(
    "--networks",
    action="store_true",
    help="Fetch NHL games from a specific date."
)


args = parser.parse_args()

if args.today == "TODAY_FLAG":
    get_games(show_broadcast=args.networks)
elif args.date:
    get_games(args.date, show_broadcast=args.networks)
else:
    get_games(show_broadcast=args.networks)