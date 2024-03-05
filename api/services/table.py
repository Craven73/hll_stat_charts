from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


def create_table(parsed_players):
    allies_players = []
    axis_players = []

    for player in parsed_players:
        player_summary = [player["name"], player["kills"], player["deaths"], player["kpm"], player["kills"] / player["deaths"] if player["deaths"] > 0 else player["kills"]]

        if player["side"] == "allies":
            allies_players.append(player_summary)
        elif player["side"] == "axis":
            axis_players.append(player_summary)


    allies_players_sorted = sorted(allies_players ,key=lambda x: x[1], reverse=True)
    axis_players_sorted = sorted(axis_players,key=lambda x: x[1], reverse=True)
    allies_players_sorted.insert(0,["Player Name", "Kills", "Deaths", "KPM", "K/D"])
    axis_players_sorted.insert(0,["Player Name", "Kills", "Deaths", "KPM", "K/D"])
    number_of_rows = max(len(allies_players_sorted), len(axis_players_sorted))
    data = []
    for ndx in range(number_of_rows):
        new_row = []
        for stat in range(4):
            if len(allies_players_sorted) >= ndx + 1:
                new_row.append(str(allies_players_sorted[ndx][stat]))
            else:
                new_row.append(" ")
        new_row.append(" ")
        for stat in range(4):
            if len(axis_players_sorted) >= ndx + 1:
                new_row.append(str(axis_players_sorted[ndx][stat]))
            else:
                new_row.append(" ")
        data.append(new_row)



    # print(allies_players_sorted)
    # print(axis_players_sorted)


    # data = [['Cell_{}_{}'.format(row, col) for col in range(9)] for row in range(50)]


    colors1 = [(60, 120, 216)] * 4 + [(204, 204, 204)] + [(204, 0, 0)] * 4
    colors2 = [(164, 194, 244)] * 4 + [(204, 204, 204)] + [(234, 153, 153)] * 4
    widths = [150, 65, 65, 65, 40, 150, 65, 65, 65]

    cell_width = 100
    cell_height = 30
    font_size = 16
    border_width = 2

    # Calculate image dimensions
    image_width = sum(widths)
    image_height = cell_height * number_of_rows

    img = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype('NotoSans-Regular.ttf', font_size)

   # Draw cells with specified colors and text
    for row, row_data in enumerate(data):
        if row == 0:
            colors = colors1
        else:
            colors = colors2
        for col, cell_data in enumerate(row_data):
            cell_width = widths[col]
            x1, y1 = sum(widths[:col]), row * cell_height
            x2, y2 = x1 + cell_width, y1 + cell_height

            # Draw cell background
            draw.rectangle([(x1, y1), (x2, y2)], fill=colors[col % len(colors)], outline='black', width=border_width)

            # Draw cell text
            text_width, text_height = draw.textsize(cell_data, font=font)
            if col == 0 or col == 5 or row == 0:
                text_x = x1 + 5
            else:
                text_x = x2 - text_width - 5
            text_y = y1 + (cell_height - text_height) / 2
            draw.text((text_x, text_y), cell_data, font=font, fill='black')



    image_stream = BytesIO()
    img.save(image_stream, format='PNG')
    image_stream.seek(0)
    return image_stream