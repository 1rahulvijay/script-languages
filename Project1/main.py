import cv2 as cv
import requests


def downloadPic():
    picLink = "https://upload.wikimedia.org/wikipedia/commons/b/b5/Warsaw_rice_mn_sign.JPG"
    response = requests.get(picLink)
    file = open("boardsign.jpg", "wb")
    file.write(response.content)
    file.close()


def run():
    downloadPic()


if __name__ == "__main__":
    run()


def mouseClick(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(ims, (x, y), 50, (100, 100, 100), -2)


img = cv.imread('warsaw.jpg', 0)
ims = cv.resize(img, (450, 450))
imr = cv.rotate(ims, cv.ROTATE_180)
imb = cv.GaussianBlur(ims, (5, 5), 0)

imw = cv.imread('boardsign.jpg', 0)
iws = cv.resize(imw, (450, 450))

cv.namedWindow('Resize')
cv.setMouseCallback('Resize', mouseClick)
result = cv.cv2.addWeighted(ims, 0.5, iws, 0.5, 0)
while 1:
    cv.imshow('Resize', ims)
    cv.imshow('Rotate_180', imr)
    cv.imshow('Gaussian Blur', imb)
    cv.imshow('Blending', result)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()
