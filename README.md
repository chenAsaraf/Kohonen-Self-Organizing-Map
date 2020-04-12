# Kohonen-Self-Organizing-Map
## 1-Dimensional topography of self-organizing map
###### Basic implementation in Python
This is a simple implementation of unsupervised network for clustering, according to Kohonen algorithm (SOM). Network's topography is a line.
*Made during Neurocomputational Cognitive Modeling Course, Ariel University.*

There are several options for data type that can be given - points that are distributed in a uniform and uneven distribution, around a certain point or in a range restriction.

- **Case number 1:**
Fit a line of neurons in a square. That is, the topology of the Kohonen level is a line. Assume the data is two dimensional (on a plane) where the points are given by (x, y) with 0<= x<=1, 0<=y<=1; and the data chosen randomly and uniformly.
When we selected more neurons (100), the line between the data points was more accurate, and the line "occupied" more space between the data points. That means there were more matches between data and the clusters.\
<p align="center">
  <b>Running with 10 neurons and the next data give the next result:</b><br>
  <br><br>
  <img src=https://github.com/chenAsaraf/Kohonen-Self-Organizing-Map/blob/master/PIC/case1.1.png>
  <img src=https://github.com/chenAsaraf/Kohonen-Self-Organizing-Map/blob/master/PIC/graph.1.1.png.
\\
  <b>Updating number of neurons to 100 increase the accuracy::</b><br>
  <br><br>
  <img src=https://github.com/chenAsaraf/Kohonen-Self-Organizing-Map/blob/master/PIC/case1.2.png>
  <img src=https://github.com/chenAsaraf/Kohonen-Self-Organizing-Map/blob/master/PIC/graph.1.2.png>
</p>

With a significant increase in the number of iterations:

![case1.3data](https://github.com/chenAsaraf/Kohonen-Self-Organizing-Map/blob/master/PIC/case1.3.png)

![case1.3graph](https://github.com/chenAsaraf/Kohonen-Self-Organizing-Map/blob/master/PIC/graph.1.3.png)



