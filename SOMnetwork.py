import numpy as np
import matplotlib.pyplot as plt
import random

# Basic parameters initialization:
# number of neurons in the pattern. in Question 1 case: a line with 100 neurons.
pattern_length = 10
# Time: increase with every new data point.
number_iteration = 100
# After some time learning rate will converge to zero.
max_time_learning_rate_update = 50
time_constant = int(0.1 * number_iteration)
# learning rate initial values:
alpha_0 = 1.0
alpha_infinte = 0.05
# initial radius:
init_rad = 5

def initialize():
    # W is an array represent the neurons by they weights.
    # each neuron has 2 coordinate
    W = np.random.normal(0.5, 1, size=(pattern_length,2))
    return W

def winning_neuron(W, data_point):
    distances = np.sqrt((W[:, 0] - data_point[0]) ** 2 + (W[:, 1] - data_point[1]) ** 2)
    winning_unit = np.argmin(distances) # index of the min distance
    return winning_unit

# This learning rate indicates how much we want to adjust our weights.
# After time max_time_learning_rate_update (positive infinite), this learning rate will converge to zero
# so we will have no update even for the neuron winner .
def learning_rate(time):
    new_learning_rate = alpha_0 * np.exp(-float(time)/ time_constant)
    # new_learning_rate = alpha_0 * np.exp(-float(time) / time_constant)
    return new_learning_rate

def radius(time):
    new_radius = float(init_rad) * np.exp(-float(time) / time_constant)
    print(new_radius)
    return new_radius

def euclidean_dist(W, point):
    dst = np.sqrt((point[0] - W[:,0]) ** 2 + (point[1] - W[:,1]) ** 2)
    return dst

# Updating weights:
# delta weights = current learning rate * neighborhood parameter * actual distance from data point
def update_location(W, data_point, winning_idx, radius, alpha):
    # ed = euclidean_dist(W, data_point)
    for node_idx in range(W.shape[0]):
        if abs(winning_idx-node_idx) < radius:
            W[node_idx] += alpha * (data_point - W[node_idx])
    return W
# Q1
def choose_uniform():
  return np.random.uniform(low=0.0, high=1.0, size=2)

# Q2
def choose_non_uniform():
    return np.random.random(size=2)

# Q3
def choose_diagonal():
    x = np.random.uniform(0.0, 1.0)
    y = x
    point = np.concatenate([x, y])
    return point

# Q4
def generate_circle_point(start_range, end_range):
  ang = np.random.uniform(low = 0.5, high = 3*np.pi, size = 1)
  r = np.random.uniform(low = start_range, high = end_range, size =1)
  y = 0.5 + r * np.sin(ang)
  x = 0.5 + r * np.cos(ang)
  point = np.concatenate([x,y])
  return point

def kohonen(question):

    data_container = np.zeros((number_iteration,2))
    W = initialize()

    for time in range(number_iteration):

        if time < max_time_learning_rate_update:
            current_learning_rate = learning_rate(time)
            current_radius = radius(time)
        else:
            current_learning_rate = 0.2
            current_radius = 1.0

        # Case 1 data:
        if question == 1 :
           data_point = choose_uniform()
        # Case 1 data:
        if question == 2 :
            data_point = choose_non_uniform()
        if question == 3 :
            data_point = choose_diagonal()
        # Case 4 data:
        if question == 4 :
            data_point = generate_circle_point(1.0, 2.0)

        data_container[time] = data_point
        closest_neuron_index = winning_neuron(W, data_point)
        W = update_location(W, data_point, closest_neuron_index, current_radius, current_learning_rate)
        # ----- draw: -------- #
        if time % 100 == 0 or time == number_iteration-1:
            print("epoch: " + str(time))
            if time == 0:
                fig, ax = plt.subplots()
            else:
                plt.clf()
                fig = plt.gcf()
                ax = fig.gca()
            ax.set(xlabel='wieght 1',
                    ylabel='wieght 2',
                    title='Kohonen algorithm (Iter: {}, Radius: {:.3f}, L_rate:{:.3f})'
                    .format(time, current_radius, current_learning_rate))
            if question == 4:
                inner_circle = plt.Circle((0.5, 0.5), 1, ec="red", fill=False)
                outer_circle = plt.Circle((0.5, 0.5), 2, ec="red", fill=False)
                plt.gca().add_patch(outer_circle)
                plt.gca().add_patch(inner_circle)
            for i in range(data_container.shape[0]):
                plt.scatter(data_container[i, 0], data_container[i, 1], color="green", s=30)
            for i in range(W.shape[0]):
                plt.scatter(W[i, 0], W[i, 1], color="blue", s=30)
            # ------ draw rings: ------ #
            # plt.plot(data_container[:, 0], data_container[:, 1], color="red", s=30)
            # plt.plt(W[:, 0], W[:, 1], color="blue", s=30)
            plt.plot(W[:, 0], W[:, 1], color='blue', linewidth=1)
            ax.grid()
            plt.pause(1.5)
            # else : plt.pause(0.5)
            plt.xlabel('x - axis')
            # frequency label
            plt.ylabel('y - axis')
            # plot title
            # plt.title('Kohonen algorithm (Iter: {%i}' % time)
    plt.show()



kohonen(2)

