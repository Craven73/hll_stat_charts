import requests
import re

def parse_logs(hlu):
    stats = {}
    response = requests.get(hlu, stream=True)
    for line in response.iter_lines(decode_unicode=True):

        
        parts = line.split("\t")
        stamp = parts[0].strip()
        event = parts[1].strip() if len(parts) >= 2 else ""
        log = parts[2].strip() if len(parts) >= 3 else ""


        if event == "KILL":
            parsed = parse_line(log)

            if not parsed:

                continue
            if parsed["steam_id1"] in stats.keys():
                player_stats = stats[parsed["steam_id1"]]
                if parsed["weapon"] in player_stats["weapon_kills"].keys():
                    player_stats["weapon_kills"][parsed["weapon"]] += 1
                else:
                    player_stats["weapon_kills"][parsed["weapon"]] = 1
                if parsed["player2"] in player_stats["victims"].keys():
                    player_stats["victims"][parsed["player2"]] += 1
                else:
                    player_stats["victims"][parsed["player2"]] = 1
            else:
                player_stats = {
                    "name": parsed["player1"],
                    "side": parsed["side1"],
                    "weapon_kills": {parsed["weapon"]: 1},
                    "victims": {parsed["player2"]: 1},
                    "weapon_deaths": {},
                    "nemesis": {}
                }
                stats[parsed["steam_id1"]] = player_stats
                if player_stats["name"] == "syn | robRRT ":
                    print(log)
                    print(parsed)
                    print(player_stats)
                    print("found myth")


            if parsed["steam_id2"] in stats.keys():
                player_stats = stats[parsed["steam_id2"]]
                if parsed["weapon"] in player_stats["weapon_deaths"].keys():
                    player_stats["weapon_deaths"][parsed["weapon"]] += 1
                else:
                    player_stats["weapon_deaths"][parsed["weapon"]] = 1
                if parsed["player1"] in player_stats["nemesis"].keys():
                    player_stats["nemesis"][parsed["player1"]] += 1
                else:
                    player_stats["nemesis"][parsed["player1"]] = 1
            else:
                player_stats = {
                    "name": parsed["player2"],
                    "side": parsed["side2"],
                    "weapon_deaths": {parsed["weapon"]: 1},
                    "nemesis": {parsed["player2"]: 1},
                    "weapon_kills": {},
                    "victims": {}
                }
                stats[parsed["steam_id2"]] = player_stats
                if player_stats["name"] == "syn | robRRT ":
                    print(log)
                    print(parsed)
                    print(player_stats)
                    print("found myth")

    return stats


def parse_line(line):
    kill_teamkill_pattern = re.compile(
        r"(.*)\((Allies|Axis)\/(\d{17})\) -> (.*)\((Allies|Axis)\/(\d{17})\) with (.*)"
    )

    if match := re.match(kill_teamkill_pattern, line):
        player1, side1, steam_id1, player2, side2, steam_id2, weapon = match.groups()
        return {
            'player1': player1,
            'side1': side1,
            'steam_id1': steam_id1,
            'player2': player2,
            'side2': side2,
            'steam_id2': steam_id2,
            'weapon': weapon
        }
    
def convert_to_rcon(stats):
    parsed_players = []
    # print(stats)
    for steam_id, player_stats in stats.items():
        parsed_player = {}
        parsed_player["name"] = player_stats["name"]
        parsed_player["side"] = player_stats["side"].lower()
        parsed_player["kills"] = sum(player_stats["weapon_kills"].values())
        parsed_player["deaths"] = sum(player_stats["weapon_deaths"].values())
        parsed_player["weapons"] = player_stats["weapon_kills"]
        parsed_player["kpm"] = " "

        parsed_players.append(parsed_player)

    return parsed_players
        