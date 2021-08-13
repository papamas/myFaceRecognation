from FaceMySQL import FaceMySQL
import face_recognition

# fr_image = face_recognition.load_image_file("198105122015031001.jpg")
# face_encodings = face_recognition.face_encodings(fr_image)
# faceSql = FaceMySQL()
# faceSql.setFace("0E2621E17314440FE050640A15023D38", face_encodings[0])
# res = faceSql.getFace("0E2621E17314440FE050640A15023D38")
# print(res)


# Load the jpg file into a numpy array
image = face_recognition.load_image_file("aku1_failed.jpg")

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
#face_locations = face_recognition.face_locations(image)

#print("I found {} face(s) in this photograph.".format(len(face_locations)))

me = [-0.13717535138130188, 0.151681050658226, 0.08774585276842117, -0.02753205969929695, -0.05840311944484711,
      -0.09863995760679245, -0.007145863026380539, -0.14810484647750854, 0.12671016156673431, -0.05781596899032593,
      0.3130040168762207, 0.005360612645745277, -0.1169147714972496, -0.23622684180736542, 0.008600239641964436,
      0.1573488712310791, -0.17190825939178467, -0.12737366557121277, -0.09507042169570923, 0.029752373695373535,
      0.13002416491508484, -0.08524281531572342, 0.09516672790050507, 0.04454105347394943, -0.03165433555841446,
      -0.41075244545936584, -0.07851631194353104, -0.10584094375371933, 0.1102944016456604, -0.05503389984369278,
      -0.0877746120095253, -0.07249283790588379, -0.24569527804851532, -0.13165155053138733, -0.050722308456897736,
      0.0920925885438919, -0.05272617191076279, -0.10033884644508362, 0.14462745189666748, -0.07274290174245834,
      -0.20511680841445923, -0.010824451223015785, 0.005473053082823753, 0.1806211620569229, 0.24387112259864807,
      0.024338841438293457, 0.11214663833379745, -0.11475474387407303, 0.10929429531097412, -0.17386825382709503,
      0.07087892293930054, 0.09314404428005219, 0.12540197372436523, 0.03664843738079071, 0.05566832050681114,
      -0.09908556193113327, 0.020888816565275192, 0.09970984607934952, -0.15962207317352295, 0.0053363973274827,
      0.06955602765083313, -0.030446354299783707, -0.042657338082790375, -0.045027121901512146, 0.23926201462745667,
      0.09790719300508499, -0.10409381985664368, -0.16513103246688843, 0.1248248890042305, -0.11979049444198608,
      -0.030788831412792206, 0.045896127820014954, -0.13725361227989197, -0.17585918307304382, -0.32732322812080383,
      0.06857171654701233, 0.4286682605743408, 0.09828067570924759, -0.18748492002487183, -0.007114584092050791,
      -0.17666049301624298, -0.010051282122731209, 0.07436252385377884, 0.08697021007537842, -0.026566850021481514,
      0.03691200911998749, -0.20533406734466553, 0.022158164530992508, 0.17100699245929718, -0.08308327943086624,
      -0.013831503689289093, 0.22075137495994568, -0.007345111109316349, 0.05052318423986435, -0.01930682547390461,
      0.05117901414632797, -0.09532824158668518, 0.11974290758371353, -0.10354933142662048, -0.004861142486333847,
      0.07911840081214905, -0.026492509990930557, -0.015878599137067795, 0.07942383736371994, -0.13331712782382965,
      0.043906066566705704, -0.017936216667294502, 0.0663975328207016, 0.031021419912576675, -0.090303935110569,
      -0.13572944700717926, -0.11956246942281723, 0.05495796725153923, -0.1821311116218567, 0.20652130246162415,
      0.21548305451869965, 0.06699448078870773, 0.11833862960338593, 0.12984076142311096, 0.06259621679782867,
      0.04735459387302399, -0.055633023381233215, -0.17631015181541443, 0.035559479147195816, 0.07346031069755554,
      -0.0004250206984579563, 0.034871913492679596, 0.024475475773215294]

fr_image = face_recognition.load_image_file("IMG_20210403_182854.jpg")
face_encodings = face_recognition.face_encodings(fr_image, None, 100, "large")
print(face_encodings)