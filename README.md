# Kohonen-Self-Organizing-Map
## 1-Dimensional topography of self-organizing map
###### Basic implementation in Python
This is a simple implementation of unsupervised network for clustering, according to Kohonen algorithm (SOM). Network's topography is a line. \
*Made during Neurocomputational Cognitive Modeling Course, Ariel University.*

There are several options for data type that can be given - points that are distributed in a uniform and uneven distribution, around a certain point or in a range restriction.

- **Case number 1:**
Fit a line of neurons in a square. That is, the topology of the Kohonen level is a line. Assume the data is two dimensional (on a plane) where the points are given by (x, y) with 0<= x<=1, 0<=y<=1; and the data chosen randomly and uniformly.
When we selected more neurons (100), the line between the data points was more accurate, and the line "occupied" more space between the data points. That means there were more matches between data and the clusters.\

Running with 10 neurons and the next data give the next result:
<p align="center">
  <img src=https://github.com/chenAsaraf/Kohonen-Self-Organizing-Map/blob/master/PIC/case1.1.png>
</p>
<p align="center">
  <img src=https://github.com/chenAsaraf/Kohonen-Self-Organizing-Map/blob/master/PIC/graph.1.1.png>
</p>

Updating number of neurons to 100 increase the accuracy:

<p align="center">
  <img src=https://github.com/chenAsaraf/Kohonen-Self-Organizing-Map/blob/master/PIC/case1.2.png>
</p>

<p align="center">
  <img src=https://github.com/chenAsaraf/Kohonen-Self-Organizing-Map/blob/master/PIC/graph.1.2.png>
</p>

With a significant increase in the number of iterations:


<p align="center">
  <img src=https://github.com/chenAsaraf/Kohonen-Self-Organizing-Map/blob/master/PIC/case1.3.png>
</p>

<p align="center">
  <img src=https://github.com/chenAsaraf/Kohonen-Self-Organizing-Map/blob/master/PIC/graph.1.3.png>
</p>


- **Case number 4:**
Data set is chosen uniformly but in the band between two concentric circles (i.e. share the same center); one of radius 1 and one of radius 2.

If we select:

<p align="center">
  <img src=https://github.com/chenAsaraf/Kohonen-Self-Organizing-Map/blob/master/PIC/case4.1.png>
</p>

<p align="center">
  <img src=https://github.com/chenAsaraf/Kohonen-Self-Organizing-Map/blob/master/PIC/graph4.101itr.jpg>
</p>

Finally after 100 iterations you can see that the line drawn between the neurons is almost entirely between the two rings, and is adjusted according to the data points.

Once again, we increased the number of iterations to 1000.  This time we also increased the initial radius. You can see that a zigzag line is created that tries to "grab" as many data points as possible.

<p align="center">
  <img src=https://github.com/chenAsaraf/Kohonen-Self-Organizing-Map/blob/master/PIC/case4.1000itr.png>
</p>

<p align="center">
  <img src=https://github.com/chenAsaraf/Kohonen-Self-Organizing-Map/blob/master/PIC/graph4.1000itr.jpg>
</p>

