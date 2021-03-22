import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np


def get_lq_image(im_path):
    try:
        img = cv.imread(im_path)
    except:
        img = im_path
    blur = cv.blur(img, (5, 5))
    return img, blur


