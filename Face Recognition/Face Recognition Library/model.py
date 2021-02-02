import numpy as np
import face_recognition as fr
import os
import io
from datetime import datetime
import cv2

path = 'images'
images = []

classNames = []
myList = os.listdir(path)

# myList.remove('.ipynb_checkpoints')
print(myList)

for image in myList:
  current_image = cv2.imread(f'{path}/{image}')
  images.append(current_image)
  classNames.append(os.path.splitext(image)[0])
print(classNames)

def perform_Encodings(images):
  encode_list = []
  for image in images:
    image_copy = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    encode_image = fr.face_encodings(image_copy)[0]
    encode_list.append(encode_image)
  return encode_list

def make_list(name):
  with open('sheet.csv', 'r+') as f:
    name_list = []
    sheet = f.readlines()
    for line in sheet:
      entry = line.split(',')
      name_list.append(entry[0])
    if name not in name_list:
      now = datetime.now()
      date_string = now.strftime('%H:%M:%S')
      f.writelines(f'\n{name},{date_string}')

encoding_list = perform_Encodings(images)
print('Process Completed')


vc = cv2.VideoCapture(0)
while True:
  
  success, image = vc.read()
  image_resize = cv2.resize(image, (0, 0), None, 0.25, 0.25)
  image_resize_copy = cv2.cvtColor(image_resize, cv2.COLOR_BGR2RGB)
  # cv2.imshow('Sample', image_resize_copy)

  faces_current_frame = fr.face_locations(image_resize_copy)
  encode_current_frame = fr.face_encodings(image_resize_copy, faces_current_frame)

  for encoded_face, face_location in zip(encode_current_frame, faces_current_frame):
    matches = fr.compare_faces(encoding_list, encoded_face)
    face_distance = fr.face_distance(encoding_list, encoded_face)
    print(face_distance)
    match_index = np.argmin(face_distance)
    if matches[match_index]:
      name = classNames[match_index].upper()
      print(name)
      y1, x2, y2, x1 = face_location
      y1, x2, y2, x1=  y1*4, x2*4, y2*4, x1*4
      cv2.rectangle(image, (x1,y1), (x2, y2), (0, 255, 0), 2)
      cv2.rectangle(image, (x1, y2 - 20), (x2, y2), (0, 255, 0))
      cv2.putText(image, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, .4, (255, 255, 255), 1)
      make_list(name)
    else:
      y1, x2, y2, x1 = face_location
      y1, x2, y2, x1=  y1*4, x2*4, y2*4, x1*4
      cv2.rectangle(image, (x1,y1), (x2, y2), (0, 255, 0), 2)
      cv2.rectangle(image, (x1, y2 - 20), (x2, y2), (0, 255, 0))
      cv2.putText(image, 'Unknown', (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, .4, (255, 255, 255), 1)

  cv2.imshow('Sample', image)
  cv2.waitKey(1)