import PIL.Image
import PIL.ImageDraw
import requests
from io import BytesIO

from IPython.display import display

import face_recognition

# Load Image
# response = requests.get("https://raw.githubusercontent.com/solegaonkar/solegaonkar.github.io/master/img/rahul1.jpeg")
# fr_image = face_recognition.load_image_file(BytesIO(response.content))
fr_image = face_recognition.load_image_file("aku.jpg")

# Identify Faces
# face_locations = face_recognition.face_locations(fr_image)

# number_of_faces = len(face_locations)
# print("I found {} face(s) in this photograph.".format(number_of_faces))

# look at the image and the face identified.
# pil_image = PIL.Image.fromarray(fr_image)

# for face_location in face_locations:
# Print the location of each face in this image. Each face is a list of co-ordinates in (top, right, bottom, left) order.
#    top, right, bottom, left = face_location
#    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
# Let's draw a box around the face
#    draw = PIL.ImageDraw.Draw(pil_image)
#    draw.rectangle([left, top, right, bottom], outline="black")

# Face Encodings
face_encodings = face_recognition.face_encodings(fr_image)
print(face_encodings)
