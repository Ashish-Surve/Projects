import simplejson as json
import urllib.request as ur
import cv2
import numpy as np

from Tesseract import reconizer13 as reco

filename = "Indian_Number_plates.json"
file = open(filename, "r")
for line in file:
    j = json.loads(line)
    print('URL is '+j['content'])
    #getting image from aws server and changing its format to req format
    url = j['content']
    url_response = ur.urlopen(url)
    img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
    #required Image
    img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)
    #Height and width
    imgheight=j['annotation'][0]['imageHeight']
    imgwidth = j['annotation'][0]['imageWidth']
    #coordinates
    coordinates=[j['annotation'][0]['points'][0]['x'],j['annotation'][0]['points'][0]['y'],j['annotation'][0]['points'][1]['x'],j['annotation'][0]['points'][1]['y']]
    #getting x and y's
    print(coordinates)
    #img = cv2.imread(img_array, cv2.IMREAD_GRAYSCALE)
    reco.image_predict(coordinates,imgwidth,imgheight,img)


