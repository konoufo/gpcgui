from flask import render_template, Response
import json

from app import app
from .dialogs import handle_folder_dialog


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/selectfolder')
def dialog():
    data = json.dumps({'folderpath': handle_folder_dialog()})
    resp = Response(data, status=200, mimetype='application/json')
    return resp
