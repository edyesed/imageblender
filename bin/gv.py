#!/usr/bin/env python
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# get Image out of pillow
from PIL import Image

# Instantiates a client
client = vision.ImageAnnotatorClient()


if __name__ == "__main__":
  # The name of the image file to annotate
  file_name = os.path.join(
      os.path.dirname(__file__),
      'resources/f_one.jpg')
  
  # Loads the image into memory
  with io.open(file_name, 'rb') as image_file:
      content = image_file.read()
  
  image_one = types.Image(content=content)
  im_one = Image.open(file_name)
  
  ### Performs label detection on the image file
  response_one = client.label_detection(image=image_one)
  labels_one = response_one.label_annotations
  #   
  print('Labels:')
  for label in labels_one:
      print(label.description)

  # Performs label detection on the image file
  face_response_one = client.face_detection(image=image_one)
  print("face_re")
  print(dir(face_response_one))
  print(face_response_one.face_annotations)

  face_one_box = face_response_one.face_annotations[0].fd_bounding_poly.vertices
  faceone_box = ( face_one_box[0].x, face_one_box[0].y, face_one_box[1].x, face_one_box[2].y )
  im_one_box = im_one.crop(faceone_box)


  file_two = os.path.join(
      os.path.dirname(__file__),
      'resources/f_two.jpg')
  
  # Loads the image into memory
  with io.open(file_two, 'rb') as image_file:
      content_two = image_file.read()
  
  image_two = types.Image(content=content_two)
  im_two = Image.open(file_two)
  
  # Performs face detection on the image file
  face_response_two = client.face_detection(image=image_two)
  print("face_re_two")
  print(face_response_two.face_annotations)
  face_box = face_response_two.face_annotations[0].fd_bounding_poly.vertices
  facetwo_box = ( face_box[0].x, face_box[0].y, face_box[1].x, face_box[2].y )
  im_two_box = im_two.crop(facetwo_box)

  # Write out the new image
  Image.blend(im_one_box, im_two_box.resize(im_one_box.size), 0.5 ).save("/tmp/comp_2.jpg")
