import cv2
import cv2.aruco as aruco
import numpy as np

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
marker_id = 0
marker_size = 400

marker = np.zeros((marker_size, marker_size), dtype=np.uint8)
aruco.drawMarker(aruco_dict, marker_id, marker_size, marker, 1)

cv2.imwrite("aruco_0.png", marker)
print("Saved aruco_0.png")

