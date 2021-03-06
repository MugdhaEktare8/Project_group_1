import cv2
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np

image = cv2.imread('Image.jpg')
image_rgb = np.copy(image)
image_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB)

image_gray = np.copy(image)
image_gray = cv2.cvtColor(image_gray, cv2.COLOR_BGR2GRAY)

max_loc_x = cv2.minMaxLoc(image_gray)[3][0]
max_loc_y = cv2.minMaxLoc(image_gray)[3][1]

s = 100
coord1 = (max_loc_x-s, max_loc_y-s)
coord2 = (max_loc_x+s, max_loc_y+s)
color = (0, 255, 255)
t = 10

image_box = np.copy(image_rgb)
image_box = cv2.rectangle(image_box, coord1, coord2, color, t)

fig, axes = plt.subplots(1, 2, figsize = (9, 12))
axes[0].imshow(image_rgb)
axes[0].set_title('Original Image');
axes[0].axis('off');
axes[1].imshow(image_box)
axes[1].set_title('Brightest Spot Detected!');
axes[1].axis('off');
