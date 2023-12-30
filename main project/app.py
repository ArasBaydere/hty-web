# app.py

from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    # coordinates.json dosyasındaki veriyi oku
    with open("coordinates.json", "r") as json_file:
        data = json.load(json_file)

    return render_template('index.html', latitude=data['latitude'], longitude=data['longitude'])

if __name__ == '__main__':
    app.run(debug=True) 