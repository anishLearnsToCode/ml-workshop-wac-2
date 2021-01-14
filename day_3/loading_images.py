import cv2

# Cv : computer vision  - opencv-python
# NLP: natural language processing nltk

I = cv2.imread('../assets/lenna.png')
# print(I[:,:,0])

len, width, channels = I.shape

# cv2.imshow('lenna blue', I[:, :, 0])
# cv2.imshow('lenna green', I[:, :, 1])
# cv2.imshow('lenna red', I[:, :, 2])
# cv2.waitKey()

I_red = I.copy()
I_blue = I.copy()
I_green = I.copy()

# B G R
# save: JPEG RGB
I_red[:, :, [0, 1]] = 0
I_blue[:,:, [1, 2]] = 0
I_green[:, :, [0, 2]] = 0

R = I_red + I_green + I_blue

# cv2.imshow('lenna  red', I_red)
# cv2.imshow('lenna  green', I_green)
# cv2.imshow('lenna  blue', I_blue)
# cv2.imshow('result', R)
cv2.imshow('subsection', I[200:400, 200:400])
cv2.waitKey()

# print(I[0:100, 0:100])

# print(I[0, 0])

# v = I.reshape((len * width * channels, 1))
# print(v.shape)
