from flask import render_template, request, jsonify
import os
import utils

UPLOAD_FOLDER = 'static/uploads'


def base():
    return render_template('base.html')


def index():
    return render_template('index.html')


def face():
    return render_template('face.html')


def encoding():
    result = {}
    if request.method == "POST":
        f = request.files['image']
        filename = f.filename
        path = os.path.join(UPLOAD_FOLDER, filename)
        f.save(path)

        face_encoding = utils.face_encoding(path, filename)
        return render_template('encoding.html', result=utils.serialize_numpy(face_encoding))

    return render_template('encoding.html')
