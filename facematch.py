import face_recognition

image_of_edward2018 = face_recognition.load_image_file('./img/myphoto/ed2018.jpg')
edward2018_face_encoding = face_recognition.face_encodings(image_of_edward2018)[0]

edward2019_image = face_recognition.load_image_file('./img/myphoto/edward2019.jpg')
edward2019_face_encoding = face_recognition.face_encodings(edward2019_image)[0]

results = face_recognition.compare_faces([edward2018_face_encoding],edward2019_face_encoding)

if results[0]:
    print("This is Edward")
else:
    print("This is not Edward")