### Project Summary

#### Objective:
The objective of the project is to identify objects on the ground within images of different rooms (kitchen, living room, and bedroom) of an apartment. This is achieved through various image processing techniques, including grayscale conversion, binary masking, contour detection, and the utilization of bounding boxes.

#### Library Usage:
The project utilizes the Python libraries OpenCV for image processing and Numpy for handling numerical data.

#### Algorithm Performance:
The algorithm developed showed promising results, successfully identifying objects on the ground. However, it struggled with images under inadequate lighting conditions or where the camera angle was drastically changed.

#### Potential Application:
This project has the potential to be improved and implemented in smart homes for the elderly to detect changes in their living environments, aiding in accident prevention and home safety.

#### Algorithm Implementation:
The `run.py` script is used to apply the `algorithm.py` to the images specified as a path. 
Example usage: `python run.py "Images"`