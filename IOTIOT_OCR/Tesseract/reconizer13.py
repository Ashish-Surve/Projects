import cv2
import pytesseract
from Tesseract import ImageTransform as it


def image_predict(image):
    # {"content": "http://com.dataturks.a96-i23.open.s3.amazonaws.com/2c9fafb0646e9cf9016473f1a561002a/77d1f81a-bee6-487c-aff2-0efa31a9925c____bd7f7862-d727-11e7-ad30-e18a56154311.jpg.jpeg",
    # "annotation":[{"label":["number_plate"],"notes":"",
    # "points":[{"x":0.7220843672456576,"y":0.5879828326180258},{"x":0.8684863523573201,"y":0.6888412017167382}],
    # "imageWidth":806,"imageHeight":466}],"extras":null}
    img = cv2.imread(image)
    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.imshow('image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    dim = (2 * img.shape[1] , 2 * img.shape[0] )                                                # change img size

    # (thresh, im_bw) = cv2.threshold(crop_img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # dst = cv2.bitwise_not(crop_img, crop_img)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_NEAREST)
    # dst=cv2.bitwise_not(im_bw,im_bw)
    # median = cv2.medianBlur(dst,1)

    transformed_img=it.canning_processing(resized)

    # text = pytesseract.image_to_string(resized)
    text = pytesseract.image_to_string(transformed_img)
    print('*'*20)
    print(text)
    print('*' * 20)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    img_coord = (0.16194331983805668, 0.8507795100222717, 0.582995951417004, 1)
    img = 'img.png'
    image_predict( img)
