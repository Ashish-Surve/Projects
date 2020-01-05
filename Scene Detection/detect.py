import numpy as np
import cv2 as cv

def FrameCapture(path):
    vobj=cv.VideoCapture(path)
    count=0
    success1=1
    success1,image1=vobj.read()
    while success1:
        success2,image2=vobj.read()
        #print(success,image)
        #cv2.imwrite("frame%d.jpg"%count,image)

        res=image2-image1
        k=np.sum(res)
        print(sum)
        #keep this at end only.
        success1,image1=success2,image2
        count+=1

if __name__=="__main__":
    FrameCapture("/home/kakarot/Downloads/dbz.mp4")        