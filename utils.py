import pickle

import face_recognition
import json
from json import JSONEncoder
import numpy

#import connect
import FaceDTO


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def serialize_numpy(appdata):
    encoded = json.dumps(appdata, cls=NumpyArrayEncoder)  # use dump() to write array into file
    return encoded


def deserialize_numpy(appdata):
    decoded = json.loads(appdata)
    return decoded


def encoding_FaceStr(image_face_encoding):
    # Convert numpy array type to list
    encoding__array_list = image_face_encoding.tolist()
    # Convert the elements in the list to a string
    encoding_str_list = [str(i) for i in encoding__array_list]
    # Splice the strings in the list
    encoding_str = ','.join(encoding_str_list)
    return encoding_str


def face_encoding(path, filename):
    fr_image = face_recognition.load_image_file(path)
    face_encodings = face_recognition.face_encodings(fr_image)
    # encoding_str = encoding_FaceStr(face_encodings[0])
    # face_register("A8ACA79748773912E040640A040269BB", face_encodings[0])
    # face_data("A8ACA79748773912E040640A040269BB")
    FaceDTO.read("A8ACA79748773912E040640A040269BB")
    return face_encodings


def face_register(pns, data):
    result = connect.face_register(pns, data)
    return result


def face_data(pns_id):
    result = connect.face_data(pns_id)
    print(result)
