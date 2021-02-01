# Face Detection using LBP Cascade Classifier
> In Local Binary Patterns (LBP), features are extracted to form a feature vector that classifies a face from a non face.
<hr>

>It compares the central pixel value to its neighbours. For each neighbor pixel
that is greater than or equal to the center pixel, it sets its value to 1, and for
the others, it sets them to 0. reads the updated pixel values (which can be
either 0 or 1) in a clockwise order and forms a binary number. Next, it
converts the binary number into a decimal number, and that decimal number
is the new value of the center pixel. We do this for every pixel in a block.Then,
it converts each block value into a histogram, so now we have gotten one
histogram for each block in an image.
<hr>
