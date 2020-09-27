import cv2
import argparse



parser = argparse.ArgumentParser(description= 'Cartoonizing an image')
parser.add_argument('image', help= 'Image which is going to be cartoonize')
args = parser.parse_args()



class Cartoonizer():
	"""Cartoonizer effect
		A class that applies a cartoon effect to an image.

	"""
	def __init__(self):
		pass

	def render(self, img_rgb):
		img_bgr = cv2.imread(img_rgb)
		img_bgr = cv2.resize(img_bgr, (640,740))

		num_iter_bilateral = 5 #bilateral filtering steps

		# Smoothing image

		img_color = img_bgr

		img_color = cv2.pyrDown(img_color)

		for _ in range(num_iter_bilateral):
			img_color = cv2.bilateralFilter(img_color, d = 9, sigmaColor= 9, sigmaSpace= 7)

		img_color = cv2.pyrUp(img_color)

		# Converting into greyscale & applying the medium blur

		img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
		img_blur = cv2.medianBlur(img_gray, ksize= 3)


		# detect edges
		img_edge = cv2.adaptiveThreshold(img_blur, 255,
										cv2.ADAPTIVE_THRESH_MEAN_C,
										cv2.THRESH_BINARY, blockSize= 9, C = 2)

		# Again converting back to RGB format

		img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)
		# cv2.imwrite("edge.png",img_edge)
		# cv2.imshow("edge RGB", img_edge)
		# cv2.waitKey(0)

		return cv2.bitwise_and(img_color, img_edge)






if  __name__ == '__main__':


	#Add an image to render function as input
	cartoon = Cartoonizer()
	cartoon_image = cartoon.render(args.image)

	cv2.imwrite("cartoon_image.png", cartoon_image)
	cv2.imshow("cartoon_image", cartoon_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
