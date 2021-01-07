import math as m
import statistics
import numpy as np
# import matplotlib.pyplot as plt
import cv2
from matplotlib import pyplot as plt




##################### Read the image
img=cv2.imread("/Users/user/Desktop/test.jpg")


##################### choose a layer of RGB and apply median blur
b,g,r = cv2.split(img)
output_img1 = b
output_img2 = g
output_img3 = r


output_img3 = cv2.medianBlur(output_img3, 15)
output_img2 = cv2.medianBlur(output_img2, 15)
output_img1 = cv2.medianBlur(output_img1, 15)




##################### apply thresholding

output_img1 = np.where(output_img1 > 120, 0,255)
output_img2 = np.where(output_img2 > 120, 0,255)
output_img3 = np.where(output_img3 > 120, 0,255)




################### Closing method erosion followed by dilation.

kernel = np.ones((7,7))

output_img1 = cv2.morphologyEx((output_img1/255), cv2.MORPH_CLOSE, kernel)
output_img2 = cv2.morphologyEx((output_img2/255), cv2.MORPH_CLOSE, kernel)
output_img3 = cv2.morphologyEx((output_img3/255), cv2.MORPH_CLOSE, kernel)






img_filtered1=(output_img1 *255).astype("uint8")
img_filtered2=(output_img2 *255).astype("uint8")
img_filtered3=(output_img3 *255).astype("uint8")



####################### detect and find the circles in the image
circles1 = cv2.HoughCircles(img_filtered1, cv2.HOUGH_GRADIENT, 1, 100,param1=15,param2=15,minRadius=200,maxRadius=300)
circles2 = cv2.HoughCircles(img_filtered2, cv2.HOUGH_GRADIENT, 1, 100,param1=25,param2=20,minRadius=250,maxRadius=350)
circles3 = cv2.HoughCircles(img_filtered3, cv2.HOUGH_GRADIENT, 1, 100,param1=30,param2=20,minRadius=180,maxRadius=300)





####################### Intialize an empty image

FINAL = np.ones((img.shape))

####################### draw circles in the image

if circles1 is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	h = np.round(circles1[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in h:
		# draw the circle in the output image
		# corresponding to the center of the circle
        # THE -1 ACTS AS A HOLE FILLING FUNCTION.
		cv2.circle(FINAL, (x, y), r-1, (255, 0, 0),-1)



if circles2 is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	hh = np.round(circles2[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in hh:
		# draw the circle in the output image
		# corresponding to the center of the circle
        # THE -1 ACTS AS A HOLE FILLING FUNCTION.
		cv2.circle(FINAL, (x, y), r-1, (0, 255, 0),-1)


if circles3 is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	hhh = np.round(circles3[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in hhh:
		# draw the circle in the output image
		# corresponding to the center of the circle
        # THE -1 ACTS AS A HOLE FILLING FUNCTION.
		cv2.circle(FINAL, (x, y), r-1, (0, 0, 255),-1)



cv2.imshow("img",FINAL)
cv2.waitKey(0)
cv2.destroyAllWindows()



################# DRAWING THE OBJECTS ON THE REAL IMAGE


if circles1 is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	h = np.round(circles1[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in h:
		# draw the circle in the output image
		# corresponding to the center of the circle
        # THE -1 ACTS AS A HOLE FILLING FUNCTION.
		cv2.circle(img, (x, y), r-1, (255, 0, 0),-1)



if circles2 is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	hh = np.round(circles2[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in hh:
		# draw the circle in the output image
		# corresponding to the center of the circle
        # THE -1 ACTS AS A HOLE FILLING FUNCTION.
		cv2.circle(img, (x, y), r-1, (0, 255, 0),-1)


if circles3 is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	hhh = np.round(circles3[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in hhh:
		# draw the circle in the output image
		# corresponding to the center of the circle
        # THE -1 ACTS AS A HOLE FILLING FUNCTION.
		cv2.circle(img, (x, y), r-1, (0, 0, 255),-1)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

