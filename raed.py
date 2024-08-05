import cv2 as cv

# img = cv.imread('Photos/cat.jpg')

# cv.imshow('Cat', img)

capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    
    if cv.waitKey(20) & 0xF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()    




cv.waitKey(0)