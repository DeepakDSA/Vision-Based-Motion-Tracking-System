import cv2
import numpy as np
import math

width, height = 640, 480
fps = 30
frames = 300

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('aruco_test.mp4', fourcc, fps, (width, height))

marker = cv2.imread("aruco_0.png")

if marker is None:
    print("ERROR: aruco_0.png not found")
    exit(1)

x, y = 120, 120

for i in range(frames):
    frame = np.ones((height, width, 3), dtype=np.uint8) * 255

    offset = int(5 * math.sin(i * 0.3))

    y_pos = y + offset

    # Ensure marker stays inside frame
    y_pos = max(0, min(y_pos, height - marker.shape[0]))

    frame[y_pos:y_pos + marker.shape[0],
          x:x + marker.shape[1]] = marker

    out.write(frame)

out.release()
print("Saved aruco_test.mp4")
