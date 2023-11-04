
# **Multiple Object Tracking in video Using Deep learning**
---


`YOLOv4_custom_v3` : Python script to train and evaluate the yolov4 model

`video_to_frame` : Python script To convert video into frames

`create_annotation_files_for_images` : Creates annotation file into yolo format from annotated images/frames

`accuracy_vs_threshold` : plots the graph of accuracz vs threshold

`result2` : Contains the output coordinates of bounding boxes of detections for each frame with their detection class


# Introduction
<p align="justify">
In this research project, the goal is to develop a deep learning method, specifically using YOLOv4 (You Only Look Once version 4), for detecting and tracking multiple objects in a video frame. The context of the project is an emergency services dispatch control room where operators need to monitor multiple screens. The aim is to reduce the workload by identifying which screens and information are most frequently used.

<img src="" width="350" height="250" align="center" />

<p align="justify">
  
<p align="justify">
YOLOv4 is a well-known object detection algorithm with several enhancements over previous versions. It is chosen for its accuracy, real-time performance, and the ability to detect a wide range of object classes. YOLOv4 incorporates features like feature pyramid networks (FPN), spatial attention modules, data augmentation, and more to improve object detection.
<p align="justify">
I have trained the YOLO algorithm on a custom dataset containing images of computer screens in the control room. This unique dataset is essential because it's specific to the project's requirements, which involve recognizing multiple objects in a single frame. The YOLOv4 model is trained on this dataset and then evaluated for its performance in detecting and tracking objects in the control room footage.


# Methods

<img src="https://github.com/shreyaskorde16/YOLOv4-Computer-Screens/blob/master/label_img.png" width="350" height="250" align="right" />
<p align="justify">
  
We used the __[labelimg tool](https://github.com/HumanSignal/labelImg)__ to annotate the images ass shown on right side and provide labels to the bounding boxes when creating the dataset. For the creation of an excellent dataset that can effectively train the model, it is essential to select high-quality, well-balanced images.
<p align="justify">
There needs to be a unique configuration file. In order to train the custom YOLO v4 model. All of the hyperparameters need to be created when creating the custom object detector are contained in the configuration file.

<p align="justify">
The parameters need to be changed in yolov4\_train.cfg and yolov4\_test.cfg are as follows:


    
- File name: yolov4.cfg
- item Number of filters: $(Number of classes + 5) \times B$
- item where, B = YOLOv4 predicts three bounding boxes for every cell of the feature map hence the value of B is 3
- item Maximum Batches = $ 2000\times Number of classes
- item Steps  = (80\%,90\% of max batches) 
- item batch = Number of images to be provided in one iteration
- Subdivisions = Number of minibatches in one batch
- The dataset contains the total 348 images. 
- Number of classes = 6
- Name of classes = [Computer screen 0, Computer screen 1, Computer screen 2, Computer screen 3, Computer screen 4, Computer screen 5]

_**For Training**_

- Batch = 32
- Subdivisions = 16
- Number of filters = 33
- Max\_batches = 12000
- steps = 9600, 10800

_**For Testing**_

- Batch = 1
- Subdivisions = 1
- Number of filters = 33
- Max\_batches = 12000
- steps = 9600, 10800

