#   / Basic :-  Reading Images & Video +++++
from asyncio import capture_call_graph

import cv2 as cv
from numpy.f2py.crackfortran import dimensionpattern

# Reading Images-----

# img = cv.imread('Images/python.png')
# img = cv.imread('Images/Tony.jpg')
# cv.imshow('Marvel' , img)
# cv.waitKey(0)

# Reading Videos------

# capture = cv.VideoCapture('Videos/animate.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Videos', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):  # 0xFF==ord('d'):  --> it's means when i press (d) then close active window (jiss window me img/video open hai)
#         break

# capture.release()
# cv.destroyAllWindows()