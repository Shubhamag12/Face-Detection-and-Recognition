## This section contains differences between Haar Cascade and LBP classifiers. 
> The notebook 'Face_Detection' compares the time taken and accuracy to find the faces in an image.
<hr>


| Algorithms    | Advantages                            | Disadvantages                            |
| ------------- |:-------------------------------------:| :---------------------------------------:|
| Haar          |                                       | 1. Computationally complex and slow
|               | 1. Low false positive rates           | 2. Longer training time                 |
|               | 2. Highly detection accuracy          | 3. Less accurate on black faces          |
|               |                                       | 4. Limitations in difficult lightening conditions  |
| LBP           | 1. Computationally simple and fast    |                                     | 
|               | 2. Shorter training time              | 1. Less accurate                          | 
|               | 3. Robust to local illumination changes | 2. Highly false positive rates         |
|               | 4. Robust to occlusion                |                                       | 
