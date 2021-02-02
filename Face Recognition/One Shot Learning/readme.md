# One Shot Learning with Siamese Networks
<hr>

Siamese networks are a special type of neural network architecture. Instead of a model
learning to classify its inputs, the neural networks learns to differentiate between two inputs.
It learns the similarity between them. Typically the similarity score is squished between 0
and 1 using a sigmoid function; wherein 0 denotes no similarity and 1 denotes full similarity.
Any number between 0 and 1 is interpreted accordingly.


>Sigmoid Function :- 1/(1 + e−x)


This network is not learning to classify an image directly to any of the output classes. Rather,
it is learning a similarity function, which takes two images as input and expresses how
similar they are.
<hr>

![Diagram](https://drive.google.com/file/d/19amSOwXhqvCziYStS1Ug8dodGWe3PFrB/view?usp=sharing)

## Tuning Hyperparameter of Siamese networks:
<hr>

When we take the euclidean distance between encoding of 3 images <b><i>(like [d(A,P) - d(A,N)])</i></b>,
this value should be <= 0. But we don't want 0 as a distance as it would create similarity
between 3 tags which we don’t want to, so what we do is define 𝛂 (known as margin) like
this:

> <b><i>d(A, P) − d(A,N) + 𝛂 <= 0</i></b>

The margin parameter pushes away <b><i>d(A,P)</i></b> and <b><i>d(A,N)</i></b> from each other so that the model
may distinguish properly.
<hr>

## Loss Function:
<hr>

> <b><i>L(A, P,N) = max(d(A, P) − d(A,N) + 𝛂, 0)</i>,</b>

> <b><i>J = Σ L(A(i), P(i), N(i))</i></b>
<hr>

## Adam Optimizer:
It is an optimization algorithm used to update network weights.
