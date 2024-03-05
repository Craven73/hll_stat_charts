import io

import matplotlib
# Allow plot rendering without GUI
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd


from constants.classification import ALLIES_WEAPONS, AXIS_WEAPONS, ALLIES_ARTY, AXIS_ARTY, ALLIES_TANK, AXIS_TANK, ALLIES_TANK_SHORT, AXIS_TANK_SHORT

def create_chart(parsed_players, title):
    allies_kills_by_inf, allies_kills_by_arty, allies_kills_by_tank, axis_kills_by_inf, axis_kills_by_arty, axis_kills_by_tank = process_kills_by_weapon(parsed_players)
    return make_chart(allies_kills_by_inf, allies_kills_by_arty, allies_kills_by_tank, axis_kills_by_inf, axis_kills_by_arty, axis_kills_by_tank, title)



def handle_side(player_weapons, side_kills_by_weapon, side_kills_by_arty, side_kills_by_tank, side_arty, side_tank, side_tank_short):

    for weapon in player_weapons:
        if weapon in side_arty:
            if weapon in side_kills_by_arty.keys():
                side_kills_by_arty[weapon] += player_weapons[weapon]
            else:
                side_kills_by_arty[weapon] = player_weapons[weapon]
        elif weapon in side_tank:
            for tank in side_tank_short:
                if tank in weapon:
                    if tank in side_kills_by_tank.keys():
                        side_kills_by_tank[tank] += player_weapons[weapon]
                    else:
                        side_kills_by_tank[tank] = player_weapons[weapon]



        else:
            if weapon in side_kills_by_weapon.keys():
                side_kills_by_weapon[weapon] += player_weapons[weapon]
            else:
                side_kills_by_weapon[weapon] = player_weapons[weapon]


def process_kills_by_weapon(parsed_players):
    allies_kills_by_inf = {}
    allies_kills_by_arty = {}
    allies_kills_by_tank = {}
    axis_kills_by_inf = {}
    axis_kills_by_arty = {}
    axis_kills_by_tank = {}

    for player in parsed_players:
        weapons = player["weapons"]

        if player["side"] == "allies":
            handle_side(weapons, allies_kills_by_inf, allies_kills_by_arty, allies_kills_by_tank, ALLIES_ARTY, ALLIES_TANK, ALLIES_TANK_SHORT)
        elif player["side"] == "axis":
            handle_side(weapons, axis_kills_by_inf, axis_kills_by_arty, axis_kills_by_tank, AXIS_ARTY, AXIS_TANK, AXIS_TANK_SHORT)

    return allies_kills_by_inf, allies_kills_by_arty, allies_kills_by_tank, axis_kills_by_inf, axis_kills_by_arty, axis_kills_by_tank


def make_chart(allies_kills_by_inf, allies_kills_by_arty, allies_kills_by_tank, axis_kills_by_inf, axis_kills_by_arty, axis_kills_by_tank, title):
    y = [str(weapon)[:12] for weapon in allies_kills_by_inf.keys()]
    allies_inf_x = [int(allies_kills_by_inf[weapon]) for weapon in allies_kills_by_inf.keys()]

    df = pd.DataFrame({
        "weapons": y,
        "kills": allies_inf_x
    }, index=y)

    allies_kills_df = df.sort_values("kills")

    allies_tank_y = [str(tank).replace("Sherman", "")[:12] for tank in allies_kills_by_tank.keys()]
    allies_tank_x = [int(allies_kills_by_tank[tank]) for tank in allies_kills_by_tank.keys()]
    allies_tank_df = pd.DataFrame({
        "weapons": allies_tank_y,
        "kills": allies_tank_x
    }, index=allies_tank_y)

    allies_tank_df = allies_tank_df.sort_values("kills")
    print(allies_kills_by_inf)
    allies_inf_total = 0
    allies_tank_total = 0
    allies_arty_total = 0
    for weapon in allies_kills_by_inf:
        allies_inf_total += allies_kills_by_inf[weapon]

    for tank in allies_kills_by_tank:
        allies_tank_total += allies_kills_by_tank[tank]

    for arty in allies_kills_by_arty:
        allies_arty_total += allies_kills_by_arty[arty]

    allies_total_kills = allies_inf_total + allies_tank_total + allies_arty_total

    labels = ["Total", "Infantry", "Arty", "Tank"]
    allies_total_df = pd.DataFrame({
        "type": labels,
        "kills": [allies_total_kills, allies_inf_total, allies_arty_total, allies_tank_total]
    }, index=labels)
    allies_total_df = allies_total_df.sort_values("kills")

    y = [str(weapon)[:12] for weapon in axis_kills_by_inf.keys()]
    axis_inf_x = [int(axis_kills_by_inf[weapon]) for weapon in axis_kills_by_inf.keys()]

    df = pd.DataFrame({
        "weapons": y,
        "kills": axis_inf_x
    }, index=y)

    axis_kills_df = df.sort_values("kills")

    axis_tank_y = [str(tank).replace("Sherman", "")[:12] for tank in axis_kills_by_tank.keys()]
    axis_tank_x = [int(axis_kills_by_tank[tank]) for tank in axis_kills_by_tank.keys()]
    axis_tank_df = pd.DataFrame({
        "weapons": axis_tank_y,
        "kills": axis_tank_x
    }, index=axis_tank_y)

    axis_tank_df = axis_tank_df.sort_values("kills")


    axis_inf_total = 0
    axis_tank_total = 0
    axis_arty_total = 0
    for weapon in axis_kills_by_inf:
        axis_inf_total += axis_kills_by_inf[weapon]

    for tank in axis_kills_by_tank:
        axis_tank_total += axis_kills_by_tank[tank]

    for arty in axis_kills_by_arty:
        axis_arty_total += axis_kills_by_arty[arty]

    axisTotalKills = axis_inf_total + axis_tank_total + axis_arty_total

    labels = ["Total", "Infantry", "Arty", "Tank"]
    axis_total_df = pd.DataFrame({
        "type": labels,
        "kills": [axisTotalKills, axis_inf_total, axis_arty_total, axis_tank_total]
    }, index=labels)
    axis_total_df = axis_total_df.sort_values("kills")


    fig, axes = plt.subplots(nrows=3, ncols=2)
    ax1 = allies_kills_df.plot.barh(ax=axes[0, 0], legend=False, title="Allies Kills by Weapon")
    ax1.bar_label(ax1.containers[0])
    ax1.set_xlim(0, max(allies_inf_x) + 100)
    ax1.set_xlabel("Kills")

    ax2 = axis_kills_df.plot.barh(ax=axes[0, 1], legend=False, title="Axis Kills by Weapon")
    ax2.bar_label(ax2.containers[0])
    ax2.set_xlim(0, max(axis_inf_x) + 100)
    ax2.set_xlabel("Kills")

    ax3 = allies_tank_df.plot.barh(ax=axes[1, 0], legend=False, title="Allies Kills by Tank")
    ax3.bar_label(ax3.containers[0])
    ax3.set_xlim(0, max(allies_tank_x) + 100)
    ax3.set_xlabel("Kills")

    ax4 = axis_tank_df.plot.barh(ax=axes[1, 1], legend=False, title="Axis Kills by Tank")
    ax4.bar_label(ax4.containers[0])
    ax4.set_xlim(0, max(axis_tank_x) + 100)
    ax4.set_xlabel("Kills")

    ax5 = allies_total_df.plot.barh(ax=axes[2, 0], legend=False, title="Allies Totals")
    ax5.bar_label(ax5.containers[0])
    ax5.set_xlim(0, allies_total_kills + 100)
    ax5.set_xlabel("Kills")

    ax6 = axis_total_df.plot.barh(ax=axes[2, 1], legend=False, title="Axis Totals")
    ax6.bar_label(ax6.containers[0])
    ax6.set_xlim(0, axisTotalKills + 100)
    ax6.set_xlabel("Kills")
    fig.set_size_inches(20, 12)
    fig.suptitle(title, fontsize=16, fontweight="bold")
    plt.subplots_adjust(top=.95, bottom=.05, hspace=.3)
    image_stream = io.BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    plt.close()

    return image_stream