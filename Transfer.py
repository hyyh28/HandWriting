from ReadData import LetterData
from PIL import Image
import numpy as np
data = LetterData()

testdata = np.mat(data.data[1]).reshape(16, 8)
print(testdata)
new_im = Image.fromarray(testdata)
new_im.show()