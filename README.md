
# **Multiple Object Tracking in video Using Deep learning**



`YOLOv4_custom_v3`: Python script to train and evaluate the yolov4 model

`video_to_frame`: Python script To convert video into frames

`create_annotation_files_for_images`: Creates annotation file into yolo format from annotated images/frames

`accuracy_vs_threshold`: plots the graph of accuracy vs threshold

`result2`: Contains the output coordinates of bounding boxes of detections for each frame with their detection class


# Introduction
<p align="justify">
In this research project, the goal is to develop a deep learning method, specifically using YOLOv4 (You Only Look Once version 4), for detecting and tracking multiple objects in a video frame. The context of the project is an emergency services dispatch control room where operators need to monitor multiple screens. The aim is to reduce the workload by identifying which screens and information are most frequently used. The flowchart below shows the procedure to reach the desired goal which is to track the multiple objects in our case which are screens in a video.  

---
<img src="https://github.com/shreyaskorde16/YOLOv4-Computer-Screens/blob/master/flowchart.png" alt="Flowchart"  title="Flowchart" width="500" height="500" align="centre" />

<p align="justify">
YOLOv4 is a well-known object detection algorithm with several enhancements over previous versions. It is chosen for its accuracy, real-time performance, and the ability to detect a wide range of object classes. YOLOv4 incorporates features like feature pyramid networks (FPN), spatial attention modules, data augmentation, and more to improve object detection. First, frame by frame, the images are taken out of the control room video clip as shown in Figure Image data.  
  <p align="justify">
<img src="https://github.com/shreyaskorde16/YOLOv4-Computer-Screens/blob/master/image_data.jpg" width="350" height="250" align="right" /> Later, the labelimg tool is used to label each of these images by creating rectangular bounding boxes and assigning classes to all of the objects of interest.  
I have trained the YOLO algorithm on a custom dataset containing images of computer screens in the control room. This unique dataset is essential because it's specific to the project's requirements, which involve recognizing multiple objects in a single frame. The YOLOv4 model is trained on this dataset and then evaluated for its performance in detecting and tracking objects in the control room footage.  As the model receives images, Images are fed into convolutional downsampling, after layers of dense connection blocks that perform various operations and calculations. The outputs from these blocks are now transferred to object detection to distinguish between the various classes in a picture before passing via a spatial pyramid pooling layer to broaden receptive fields.


# Methods

<img src="https://github.com/shreyaskorde16/YOLOv4-Computer-Screens/blob/master/label_img.png" width="400" height="300" align="right" />
<p align="justify">
  
We used the __[labelimg tool](https://github.com/HumanSignal/labelImg)__ to annotate the images as shown on the right side and provide labels to the bounding boxes when creating the dataset. For the creation of an excellent dataset that can effectively train the model, it is essential to select high-quality, well-balanced images.
<p align="justify">
There needs to be a unique configuration file. In order to train the custom YOLO v4 model. All of the hyperparameters that need to be created when creating the custom object detector are contained in the configuration file.

<p align="justify">
The parameters need to be changed in yolov4\_train.cfg and yolov4\_test.cfg are as follows:


    
- File name: yolov4.cfg
- item Number of filters: $(Number of classes + 5) \times B$
- item where B = YOLOv4 predicts three bounding boxes for every cell of the feature map hence the value of B is 3
- item Maximum Batches = $ 2000\times Number of classes
- item Steps  = (80\%,90\% of max batches) 
- item batch = Number of images to be provided in one iteration
- Subdivisions = Number of mini-batches in one batch
- The dataset contains a total of 348 images. 
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


# Result Analysis

  <img src="https://github.com/shreyaskorde16/YOLOv4-Computer-Screens/blob/master/predictions_collage_6.jpg" width="400" height="325" align="right" />
<p align="justify">
We mainly concentrate on the accuracy of finding the correct computer screen while minimizing miss detections when analyzing the YOLO model that we have trained for multiple object detection. We initially evaluate the outcomes and map the model's correctness by adjusting the confidence score threshold. The Yolo algorithm divides the image into grid cells before predicting the bounding boxes and class probabilities for each grid cell's objects using the confidence threshold. The confidence threshold is the minimal boundary value required in determining whether or not predicted bounding boxes should be taken into account for valid detection. We were able to acquire the outcome data in the form of video detections by increasing the threshold from 30% to 99%.

<p align="justify">
We discovered different accuracies for distinct computer screen classes by doing the same procedure for each confidence threshold. The graph of Accuracy vs Threshold is shown below. presents a better concept for getting the best outcomes for a specific threshold with fewer miss detections. 


# **Conclusion**
<p align="justify">
  <img src="https://github.com/shreyaskorde16/YOLOv4-Computer-Screens/blob/master/accuracy_vs_thre_final.png" width="400" height="325" align="right" />
Multiple object detection in images and videos is a difficult task. We employed the YOLO v4 object detection model and successfully used it to locate and track multiple computer screens in an egocentric video of an emergency services dispatch control room. Based on the accuracy vs. threshold graph shown in the accuracy vs threshold Figure above. we are able to conclude that executing the model at a threshold of 65-70 offered the best results, with fewer miss detections. By doing so, we are able to retrieve critical information far faster than a control room operator. As a result, we may reduce human error in emergency service dispatch and increase the efficiency of those working in the control room. This device identifies computer screens with an accuracy that varies between 98 and 99 percent. If the video contains other computer screens, such as a laptop screen with different information on it or a mobile phone, our model will struggle to track them because it has not been trained to recognize laptop and mobile phone screens.
