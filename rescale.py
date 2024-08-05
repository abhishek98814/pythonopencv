import cv2 as cv;

# img = cv.imread('Photos/cat_larget2.jpg')
# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[1] * scale)
         
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    
    frame_resized = rescaleFrame(frame)

    cv.imshow('video', frame)
    cv.imshow('video_Resized', frame_resized)

    if cv.waitKey(20) & 0xF==ord('d'):
        break

capture.release()
cv.destroyAllWindows() 