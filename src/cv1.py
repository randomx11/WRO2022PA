# Python code for Multiple Color Detection 
import time

import cv2
import numpy as np
import serial

red_detected = False
green_detected = False
start = False

# Capturing video through webcam and arduino comms.
webcam = cv2.VideoCapture(5) 
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.01)
    data = arduino.readline()
    return data

# Start a while loop 
while(1):
		# Reading the video from the 
		# webcam in image frames 
		_, imageFrame = webcam.read() 
		# Convert the imageFrame in s
		# BGR(RGB color space) to 
		# HSV(hue-saturation-value) 
		# color space 
		hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 

		# Set range for red color and 
		# define mask
		#red_lower = np.array([0, 87, 111], np.uint8)
		#red_upper = np.array([10, 255, 255], np.uint8)
		red_lower = np.array([136, 87, 111], np.uint8)
		red_upper = np.array([180, 255, 255], np.uint8)
		red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
		# decrease sensitivity of red color
		red_mask = cv2.erode(red_mask, None, iterations=10)
		red_mask = cv2.dilate(red_mask, None, iterations=10)

		# Set range for green color and 
		# define mask

		green_lower = np.array([31, 36, 35], np.uint8)
		green_upper = np.array([70, 255, 255], np.uint8)
		green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)
		# decrease sensitivity of green mask
		green_mask = cv2.erode(green_mask, None, iterations=12)
		green_mask = cv2.dilate(green_mask, None, iterations=12)

		# Morphological Transform, Dilation 
		# for each color and bitwise_and operator 
		# between imageFrame and mask determines 
		# to detect only that particular color 
		kernal = np.ones((5, 5), "uint8") 
		
		# For red color 
		red_mask = cv2.dilate(red_mask, kernal) 
		res_red = cv2.bitwise_and(imageFrame, imageFrame, 
								mask = red_mask) 
		
		# For green color 
		green_mask = cv2.dilate(green_mask, kernal) 
		res_green = cv2.bitwise_and(imageFrame, imageFrame, 
									mask = green_mask) 

		# Creating contour to track red color 
		contours, hierarchy = cv2.findContours(red_mask, 
											cv2.RETR_TREE, 
											cv2.CHAIN_APPROX_SIMPLE) 
		
		for pic, contour in enumerate(contours): 
			area = cv2.contourArea(contour) 
			if(area > 300): 
				x, y, w, h = cv2.boundingRect(contour)
				red_detected = True
				imageFrame = cv2.rectangle(imageFrame, (x, y), 
										(x + w, y + h), 
										(0, 0, 255), 2) 
				
				cv2.putText(imageFrame, "Red Colour", (x, y), 
							cv2.FONT_HERSHEY_SIMPLEX, 1.0, 
							(0, 0, 255))	 

		# Creating contour to track green color 
		contours, hierarchy = cv2.findContours(green_mask, 
											cv2.RETR_TREE, 
											cv2.CHAIN_APPROX_SIMPLE) 
		
		for pic, contour in enumerate(contours): 
			area = cv2.contourArea(contour) 
			if(area > 300): 
				x, y, w, h = cv2.boundingRect(contour)
				green_detected = True
				imageFrame = cv2.rectangle(imageFrame, (x, y), 
										(x + w, y + h), 
										(0, 255, 0), 2) 
				
				cv2.putText(imageFrame, "Green Colour", (x, y), 
							cv2.FONT_HERSHEY_SIMPLEX, 
							1.0, (0, 255, 0))
		
		# Showing the imageFrame
		cv2.imshow("Blocks Detection", imageFrame)
		time.sleep(0.1)
		write_read("a")
		if cv2.waitKey(10) & 0xFF == ord('q'): 
			cv2.destroyAllWindows()
			break
		
		if(red_detected == True):
			write_read("130")
			red_detected = False

		elif(green_detected == True):
			write_read("60")
			green_detected = False