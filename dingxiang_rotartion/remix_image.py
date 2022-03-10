import numpy as np
from PIL import Image
import cv2

openpath1 = "C:/Users/Dero/Desktop/dx/1.png"
openpath2 = "C:/Users/Dero/Desktop/dx/2.png"

image1 = Image.open(openpath1)
image2 = Image.open(openpath2)

img_array1 = np.asarray(image1)
img_array2 = np.asarray(image2)

print(img_array1.shape)
print(img_array2.shape)

for i in range(0, 160):
    for j in range(0, 160):
        if (i - 80) ** 2 + (j - 80) ** 2 <= 69 ** 2:
            img_array2[i+20][j+120] = img_array1[i][j]

# for i in range(0, 200):
#     for j in range(0, 400):
#         if (i - 100) ** 2 + (j - 200) ** 2 <= 80 ** 2:
#             img_array2[i][j] = 200


Image.fromarray(np.uint8(img_array2))
img_save = cv2.cvtColor(np.asarray(img_array2), cv2.COLOR_RGB2BGR)
savapath = "C:/Users/Dero/Desktop/dx/8.png"
cv2.imwrite(savapath, img_save)

