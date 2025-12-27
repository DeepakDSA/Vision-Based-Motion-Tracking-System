📌 Overview

This repository contains a local-host prototype of a vision-based motion tracking system developed using C++ and OpenCV.

The implementation was built and tested on a local Linux machine to:

Verify compilation and runtime correctness

Understand and validate the processing pipeline

Prepare for deployment on NVIDIA Jetson platforms

The system uses camera-based tracking and currently supports ArUco marker detection, with planned extension to Digital Image Correlation (DIC) methods.




✨ Current Features

✅ Local-host execution (non-Jetson)

✅ OpenCV-based camera capture

✅ ArUco marker detection and tracking

✅ Multithreaded frame processing

✅ ROI-based motion estimation

⚠️ Performance not yet optimized for embedded hardware

🛠️ Technologies Used

C++17

OpenCV (aruco module)

GStreamer

CMake
