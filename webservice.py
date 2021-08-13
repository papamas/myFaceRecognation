# This is a _very simple_ example of a web service that recognizes faces in uploaded images.
# Upload an image file and it will check if the image contains a picture of Barack Obama.
# The result is returned as json. For example:
#
# $ curl -XPOST -F "file=@obama2.jpg" http://127.0.0.1:5001
#
# Returns:
#
# {
#  "face_found_in_image": true,
#  "is_picture_of_obama": true
# }
#
# This example is based on the Flask file upload example: http://flask.pocoo.org/docs/0.12/patterns/fileuploads/

# NOTE: This example requires flask to be installed! You can install it with pip:
# $ pip3 install flask
import numpy as np
import cv2
import json
import os
import face_recognition
import mysql
from flask import Flask, jsonify, request, redirect

# You can change this to any folder on your system
from FaceMySQL import FaceMySQL

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.jpeg','gif']
app.config['imgdir'] ="./face"

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    # Check if a valid image file was uploaded
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        file_ext = os.path.splitext(file.filename)[1]
        if file_ext not in current_app.config['UPLOAD_EXTENSIONS']:
            return jsonify(error=str(e)), 400

        if file:
            # The image file seems valid! Detect faces and return the result.
            return detect_faces_in_image(file)

    # If no valid image file was uploaded, show the file upload form:
    return '''
    <!doctype html>
    <title>Is this a picture of Obama?</title>
    <h1>Upload a picture and see if it's a picture of Obama!</h1>
    <form method="POST" enctype="multipart/form-data" action="faceDetect">
      <input type="file" name="file">
      <input type="text" name="pns" value="0E2621E17314440FE050640A15023D38">
      <input type="submit" value="Upload">
    </form>
    '''


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify(error=str(e)), 405


@app.errorhandler(500)
def method_not_allowed(e):
    return jsonify(error=str(e)), 500


@app.route('/faceDetect', methods=['POST'])
def faceDetect():
    # Check if a valid image file was uploaded
    if request.method == 'POST':
        if 'file' not in request.files:
            result = {
                "message": "No input File",
                "status": False
            }
            return jsonify(result)

        if 'pns' not in request.form:
            result = {
                "message": "No input PNS",
                "status": False
            }
            return jsonify(result)

        file = request.files['file']
        pns = request.form.get('pns')

        if file.filename == '':
            result = {
                "message": "Please upload a File",
                "status": False
            }
            return jsonify(result)

        if not pns:
            result = {
                "message": "Input PNS",
                "status": False
            }
            return jsonify(result)

        file_ext = os.path.splitext(file.filename)[1].lower()
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            result = {
                "message": "File Not Support",
                "status": False
            }
            return jsonify(result)

        if file and pns:
            # The image file seems valid! Detect faces and return the result.
            return detect_faces_in_image(pns, file)


@app.route('/faceEncoding', methods=['POST'])
def faceEncoding():
     # Check if a valid image file was uploaded
     if request.method == 'POST':
        if 'file' not in request.files:
            result = {
                "message": "No input File",
                "status": False
            }
            return jsonify(result)

        if 'pns' not in request.form:
            result = {
                "message": "No input PNS",
                "status": False
            }
            return jsonify(result)

        file = request.files['file']
        pns = request.form.get('pns')

        if file.filename == '':
            result = {
                "message": "Please upload a File",
                "status": False
            }
            return jsonify(result)

        if not pns:
            result = {
                "message": "Input PNS",
                "status": False
            }
            return jsonify(result)

        file_ext = os.path.splitext(file.filename)[1].lower()
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            result = {
                "message": "File not support",
                "status": False
            }
            return jsonify(result)

        if file and pns:
            # The image file seems valid! Detect faces and return the result.
            return face_encoding(pns, file)

def create_opencv_image_from_stringio(img_stream, cv2_img_flag=0):
    img_stream.seek(0)
    img_array = np.asarray(bytearray(img_stream.read()), dtype=np.uint8)
    return cv2.imdecode(img_array, cv2_img_flag)


def detect_faces_in_image(pns, file_stream):
    # Pre-calculated face encoding of Obama generated with face_recognition.face_encodings(img)
    # Load the uploaded image file
    #filename = file_stream.filename  # save file
    #filepath = os.path.join(app.config['imgdir'], filename);
    #file_stream.save(filepath)
    #img = cv2.imread(filepath)
    img = create_opencv_image_from_stringio(file_stream)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #img = face_recognition.load_image_file(img)
    # Get face encodings for any faces in the uploaded image
    #boxes = face_recognition.face_locations(rgb, model='hog')
    #unknown_face_encodings = face_recognition.face_encodings(rgb,boxes)
    unknown_face_encodings = face_recognition.face_encodings(rgb)
    try:
        faceSQL = FaceMySQL()
        face = faceSQL.getFace(pns)
        # fetch result
        row = faceSQL.row()
        num = faceSQL.num_rows()
        if num > 0:
            face = json.loads(row[0])
        else:
            face = [-1.37175351e-01]
    except mysql.connector.Error as error:
        print("Failed to getFace: {}".format(error))
    finally:
        faceSQL.close()
    known_face_encoding = face
    face_found = False
    is_me = False
    message = "Kami tidak dapat mengenali wajah anda"

    if len(unknown_face_encodings) > 0:
        face_found = True
        # See if the first face in the uploaded image matches the known face of Obama
        match_results = face_recognition.compare_faces([known_face_encoding], unknown_face_encodings[0])
        if match_results[0]:
            is_me = True
            message = "Kami berhasil mengenali wajah anda"

    # Return the result as json
    result = {
        "status": True,
        "message": message,
        "face_found_in_image": face_found,
        "is_me": is_me
    }
    return jsonify(result)


def face_encoding(pns, file_stream):
    try:
        img = create_opencv_image_from_stringio(file_stream)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(rgb)

        face_encoded = False
        face_update = False
        faceSQL = FaceMySQL()

        # cek data existing
        faceSQL.getFace(pns)
        # Fetch Result
        faceSQL.row()
        num = faceSQL.num_rows()
        if num > 0:
            faceSQL.updateFace(pns, face_encodings[0])
            face_update = True
        else:
            faceSQL.setFace(pns, face_encodings[0])

        faceSQL.commit()
        faceSQL.close()

        if len(face_encodings) > 0:
            face_encoded = True

        result = {
            "status": True,
            "message": "success",
            "face_encoded": face_encoded,
            "face_encoding": json.dumps(face_encodings[0].tolist()),
            "pns": pns,
            "face_update": face_update
        }

    except mysql.connector.Error as error:
        print("Failed to setFace: {}".format(error))
        result = {
            "status": True,
            "message": format(error),
            "face_encoded": face_encoded,
            "face_encoding": "",
            "pns": pns,
            "face_update": face_update
        }

    return jsonify(result)


if __name__ == "__main__":
    # ,ssl_context=('/etc/letsencrypt/live/satupintu.my.id/fullchain.pem', '/etc/letsencrypt/live/satupintu.my.id/privkey.pem')
    app.run(host="0.0.0.0", port=5001, debug=True)
