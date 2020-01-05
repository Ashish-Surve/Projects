import simplejson as json
import urllib.request as ur
import cv2
import numpy as np

filename = "Indian_Number_plates.json"
file = open(filename, "r")
i=1
# for line in file:
#     j = json.loads(line)
#     print('URL is '+j['content'])
#     #getting image from aws server and changing its format to req format
#     url = j['content']
#     url_response = ur.urlopen(url)
#     img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
#     #required Image
#     img = cv2.imdecode(img_array,cv2.IMREAD_COLOR)
#     cv2.imwrite('/home/kakarot/Documents/Projects/NumberPlateReco/DataSet/image'+str(i)+'.jpeg', img)
#     i=i+1


