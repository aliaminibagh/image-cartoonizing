import cv2
import tkinter as tk
from tkinter.filedialog import askopenfile


class Cartoonizer:
	"""Cartoonizer effect
		A class that applies a cartoon effect to an image.

	"""
	def __init__(self):
		pass

	def render(self, img_rgb):
		img_rgb = cv2.imread(img_rgb)
		img_rgb = cv2.resize(img_rgb, (800,640))

		num_iter  = 5 #bilateral filtering steps

		# Smoothing image

		img_color = img_rgb
		img_color = cv2.pyrDown(img_color)

		for _ in range(num_iter ):
			img_color = cv2.bilateralFilter(img_color, d = 9, sigmaColor= 9, sigmaSpace= 7)

		img_color = cv2.pyrUp(img_color)

		# Converting into greyscale & applying the medium blur

		img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
		img_blur = cv2.medianBlur(img_gray, ksize= 3)


		# detect edges
		img_edge = cv2.adaptiveThreshold(img_blur, 255,
										cv2.ADAPTIVE_THRESH_MEAN_C,
										cv2.THRESH_BINARY, blockSize= 9, C = 2)
		# cv2.imshow("edge image",img_edge)
		# cv2.waitKey(0)

		# Again converting back to RGB format

		img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
		# cv2.imwrite("edge.png",img_edge)
		# cv2.imshow("edge RGB", img_edge)
		cv2.waitKey(0)

		return cv2.bitwise_and(img_color, img_edge)






if  __name__ == '__main__':


	#Add an image to render function as input
	cartoon = Cartoonizer()
	cartoon_image = cartoon.render("pexels.jpg")

	cv2.imwrite("cartoon_image.png", cartoon_image)
	cv2.imshow("cartoon_image", cartoon_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
