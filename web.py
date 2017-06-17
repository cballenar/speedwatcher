import json
from flask import Flask, render_template, request, abort, redirect, jsonify, send_from_directory
from flask_restful import Resource, Api
from speedwatcher import SpeedWatcher

app = Flask(__name__)
api = Api(app)


# define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('assets', path)

@app.route('/api/get', methods=['POST'])
def get_report():
    date_start = request.form['date_start']
    date_end = request.form['date_end']
    period_type = request.form['period_type']
    data_type = request.form['data']

    s = SpeedWatcher(date_start, date_end)
    data = s.get_data(data_type, period_type)

    return render_template('report.html', messages=data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)