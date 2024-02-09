# Object Detection using OpenCV
 
Usage of script and algorithm: 
The run.py script that we developed iterates through all folders and files starting from the address of an initial folder. It applies the object detection algorithm algorithm.py to all found files. 

Reference image handling: 
The algorithm assumes that a reference image is located in the same folder as the images to be processed. If it is absent, no processing is done. 

Script usage mode: 
The final Python script run.py takes as arguments the address of a folder containing images and a reference image. For example, the Image folder or the Image\Cuisine folder could be passed as arguments.

Example usage:
python .\run.py ".\Images\"