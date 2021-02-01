# Face Detection using Haar Cascade Classifier
> It is an ML based approach which is trained from many many positive (with faces) and negative images (without faces).
<hr>

## Haar Like Features
> Haar like features are image features that we use in object detection. Each window is placed on the picture to calculate a single feature. For example if we want to recognize a face, we’ll first convert it into a grayscale
image and find out the black and white regions. If we look carefully we find that the region near eyes is black and the nose bridge is somewhat white. 
So the face is detected by calculating the difference between the sum of pixels under white part and the sum of pixels under black part in that region, that is,
the feature. If it is near 255, then it is positive, else negative. We discard the features that are irrelevant and keep only relevant features by a technique called AdaBoost. It is a training process for face detection, which
selects only those features known to improve the classification (face/non-face) accuracy of our classifier.
<hr>

## To read the original documentation, click [here](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)
