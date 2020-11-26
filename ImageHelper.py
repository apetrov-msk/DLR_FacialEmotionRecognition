import numpy as np
from PIL import Image


def showNumpyImg(numpyImg):
    Image.fromarray(numpyImg, 'RGB').show()


def NumpyImg2Tensor(numpyImg):
    return np.expand_dims(numpyImg, axis=0)
