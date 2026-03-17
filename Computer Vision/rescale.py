#  /Basic :-  Resizing & Rescaling....

import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Reading Videos
capture = cv.VideoCapture('Videos/animate.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.40)  # Resize frame size into 40%

    cv.imshow('Videos', frame)
    cv.imshow('Videos Resized' , frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):  # 0xFF==ord('d'):  --> it's means when i press (d) then close active window (jiss window me img/video open hai)
        break

capture.release()
cv.destroyAllWindows()