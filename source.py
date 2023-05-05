import cv2
from tkinter.filedialog import askopenfilename
import numpy as np

signedfile = askopenfilename(title="Signed file")

if signedfile == "":
    exit(0)

signed = cv2.imread(signedfile)
signwidth, signheight = signed.shape[1], signed.shape[0]
signedout = np.zeros((signheight,signwidth,3), np.uint8)

for row in range(signheight):
    for pixel in range(signwidth):
        signedbit = signed[row][pixel][0] & 1
        if signedbit == 1:
            signedout[row][pixel] = (255,255,255)
        else:
            signedout[row][pixel] = (0,0,0)

cv2.imwrite('out/signout.png', signedout)
