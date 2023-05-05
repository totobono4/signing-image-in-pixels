import cv2
from tkinter.filedialog import askopenfilename
import numpy as np

imagefile = askopenfilename(title="Image to sign")
signaturefile = askopenfilename(title="Signature image")

if imagefile == "" or signaturefile == "":
    exit(0)

image = cv2.imread(imagefile)
signature = cv2.imread(signaturefile)

signature = cv2.resize(signature, (image.shape[1], image.shape[0]))
signwidth, signheight = signature.shape[1], signature.shape[0]

for row in range(signheight):
    for pixel in range(signwidth):
        if signature[row][pixel][0] > 0 or signature[row][pixel][1] > 0 or signature[row][pixel][2] > 0:
            signature[row][pixel] = (255,255,255)
            image[row][pixel][0] = image[row][pixel][0] | 1
        else :
            signature[row][pixel] = (0,0,0)
            image[row][pixel][0] = image[row][pixel][0] & 254

cv2.imwrite('out/signed.png', image)
cv2.imwrite("out/sign.png", signature)
