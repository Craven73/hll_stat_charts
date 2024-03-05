from flask import render_template, request, send_file, Response
from app import app

from services.rcon_url import retrieve_gameboard, parse_rcon_json
from services.charts import  create_chart, process_kills_by_weapon
from services.table import create_table
from services.logs import parse_logs, convert_to_rcon

@app.route('/rcon-url/chart', methods=['POST'])
def rcon_url_chart():
    data = request.get_json()
    gameboard = data.get('gameboard')
    title = data.get('title')
    override = data.get('override')
    # print(gameboard)
    gameboard_data = retrieve_gameboard(gameboard)
    parsed_players, unknown_players, unknown_weapons = parse_rcon_json(gameboard_data)

    chart = create_chart(parsed_players, title)

    return send_file(chart, mimetype='image/png')

@app.route('/rcon-url/table', methods=['POST'])
def rcon_url_table():
    data = request.get_json()
    gameboard = data.get('gameboard')
    override = data.get('override')
    # print(gameboard)
    gameboard_data = retrieve_gameboard(gameboard)
    parsed_players, unknown_players, unknown_weapons = parse_rcon_json(gameboard_data)

    table = create_table(parsed_players)
    # return "hello"
    return send_file(table, mimetype='image/png')

@app.route('/hlu/chart', methods=['POST'])
def hlu_chart():
    data = request.get_json()
    logs = data.get('logs')
    title = data.get('title')
    stats_from_logs = parse_logs(logs)
    rcon_like_stats = convert_to_rcon(stats_from_logs)

    chart = create_chart(rcon_like_stats, title)

    return send_file(chart, mimetype='image/png')

@app.route('/hlu/table', methods=['POST'])
def hlu_table():
    data = request.get_json()
    logs = data.get('logs')
    title = data.get('title')
    stats_from_logs = parse_logs(logs)
    rcon_like_stats = convert_to_rcon(stats_from_logs)

    table = create_table(rcon_like_stats)
    # return "hello"
    return send_file(table, mimetype='image/png')

@app.route('/test', methods=['GET'])
def test():
    return "this is a test"

def multiple_file_generator(*file_streams):
    boundary = 'boundary'
    for file_stream in file_streams:
        yield f'--{boundary}\r\n'
        yield 'Content-Disposition: attachment; filename={}\r\n'.format(file_stream.filename)
        yield 'Content-Type: {}\r\n\r\n'.format(file_stream.content_type)
        yield file_stream.read()
        yield '\r\n'

    yield f'--{boundary}--\r\n'