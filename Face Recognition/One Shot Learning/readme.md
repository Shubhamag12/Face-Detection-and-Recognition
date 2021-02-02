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

![Siamese Network](https://miro.medium.com/max/875/1*23mikUF3HBJGUqrX7tMKQQ.png)

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

![Loss Function](https://miro.medium.com/max/875/1*H_tT3SS13ZykLPocXuqwSw.png)

> <b><i>L(A, P,N) = max(d(A, P) − d(A,N) + 𝛂, 0)</i></b>

> <b><i>J = Σ L(A(i), P(i), N(i))</i></b>
<hr>

## Adam Optimizer:
It is an optimization algorithm used to update network weights.

## To read the research paper, click [here](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf)
