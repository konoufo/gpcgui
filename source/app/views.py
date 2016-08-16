<<<<<<< HEAD
from flask import render_template, Response
import json

from app import app
from .dialogs import handle_folder_dialog

=======
from flask import render_template

from app import app
>>>>>>> 38170fbb19cf0385bdcf157b3a2ece4235e46a8b

@app.route('/')
@app.route('/index')
def index():
<<<<<<< HEAD
    return render_template('index.html')


@app.route('/selectfolder')
def dialog():
    data = json.dumps({'folderpath': handle_folder_dialog()})
    resp = Response(data, status=200, mimetype='application/json')
    return resp
=======
    return render_template('base.html')
>>>>>>> 38170fbb19cf0385bdcf157b3a2ece4235e46a8b
