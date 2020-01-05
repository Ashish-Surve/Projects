# Transform image in a form so that tesseract can use it

import cv2


# used to find edges
def canning_processing(img):
    image = img  # read in the image
    #image = cv2.resize(image, (800, 400))  # resizing because opencv does not work well with bigger images
    orig = image.copy()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # RGB To Gray Scale
    cv2.imshow("Title", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Blur when image quality is low.
    # blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    # (5,5) is the kernel size and 0 is sigma that determines the amount of blur
    # cv2.imshow("Blur", blurred)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    edged = cv2.Canny(gray, 30,  50)  # 30 MinThreshold and 50 is the MaxThreshold
    cv2.imshow("Canny", edged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # image, contours = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # retrieve the contours as a list, with simple apprximation model
    # contours = sorted(contours, key=cv2.contourArea, reverse=True)

    ret, thresh = cv2.threshold(edged, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    return gray
