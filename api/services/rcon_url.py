import requests

from constants.classification import ALLIES_WEAPONS, AXIS_WEAPONS

URI = "/api/get_map_scoreboard?map_id="

def retrieve_gameboard(gameboard_url):
    game_number = gameboard_url.split("/")[-1]
    rcon_host = gameboard_url.split("/#/")[0]

    r = requests.get(rcon_host + URI + game_number, verify=False)
    # r = requests.get(rcon_host + URI + game_number)

    stats = r.json()["result"]["player_stats"]
    
    return stats


def parse_rcon_json(rcon_data):

    unknown_weapons = []
    unknown_players = []
    parsed_players = []

    allies_players = []
    axis_players = []

    # First Pass
    # Parse player data and try and determine side by weapon kills
    for player in rcon_data:
        parsed_player = {}
        parsed_player["name"] = player["player"]
        parsed_player["weapons"] = player["weapons"]
        parsed_player["kills"] = player["kills"]
        parsed_player["kills_streak"] = player["kills_streak"]
        parsed_player["kpm"] = player["kills_per_minute"]
        parsed_player["deaths"] = player["deaths"]
        parsed_player["teamkills"] = player["teamkills"]
        parsed_player["dpm"] = player["deaths_per_minute"]
        parsed_player["kd"] = player["kill_death_ratio"]
        parsed_player["victim"] = player["most_killed"]
        parsed_player["nemesis"] = player["death_by"]
        parsed_player["id"] = player["id"]

        weapon_dict = player["weapons"]

        side = 0

        for weapon in weapon_dict.keys():
            if weapon in ALLIES_WEAPONS:
                side += 1
            elif weapon in AXIS_WEAPONS:
                side -= 1
            else:
                if weapon not in unknown_weapons:
                    unknown_weapons.append(weapon)

        if side > 0:
            parsed_player["side"] = "allies"
            allies_players.append(player["player"])
        elif side < 0:
            parsed_player["side"] = "axis"
            axis_players.append(player["player"])
        else:
            parsed_player["side"] = "unknown"
        
        parsed_players.append(parsed_player)


    # Second Pass
    # Try and determine side based off victim and nemesis
    for player in parsed_players:
        if player["side"] == "unknown":
            # print(player)
            
            side = 0

            for vict in player["victim"]:
                if vict in axis_players:
                    side += 1
                elif vict in allies_players:
                    side -= 1

            for nem in player["nemesis"]:
                if nem in axis_players:
                    side += 1
                elif nem in allies_players:
                    side -= 1

            if side > 0:
                player["side"] = "allies"
            elif side < 0:
                player["side"] = "axis"
            else:
                unknown_players.append({"id": player["id"], "name": player["name"]})



    return parsed_players, unknown_players, unknown_weapons
