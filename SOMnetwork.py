import numpy as np
import matplotlib.pyplot as plt
import random

# Basic parameters initialization:
# number of neurons in the pattern. in Question 1 case: a line with 100 neurons.
pattern_length = 10 # (for now its easy to use 10 neurons)
# Time: increase with every new data point. 10,000
number_iteration = 100  # (for now its easy to use 100)
# After some time learning rate will converge to zero. 1,500
max_time_learning_rate_update = 1500
time_constant = int(0.1 * number_iteration) # = TAU IN LECTURE
# learning rate initial values:
alpha_0 = 1.0 # = ETA IN LECTURE
alpha_infinte = 0.05
# initial radius: 50
init_rad = 5 # = SIGMA IN LECTURE

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
    new_learning_rate = alpha_0 * np.exp(-float(time)/ number_iteration)
    # new_learning_rate = alpha_0 * np.exp(-float(time) / time_constant)
    return new_learning_rate

def radius(time):
    new_radius = float(init_rad) * np.exp(-float(time) / time_constant)
    return new_radius


# This function returns the value of the radial basis function for the whole map.
# Given: the center point (the winning unit),
#        the current value of the radius
# Adopting a radial basis function, it’s not necessary to compute an actual neighbourhood.
# Because the multiplication factor N becomes close to zero outside of the boundaries
def neighborhood_value(W, winner, current_radius):
    distances_from_winner = np.sqrt((W[:,0] - winner[0]) ** 2 + (W[:,1] - winner[1]) ** 2)
    # distances_from_winner = np.power((winner - W),2)
    denominator = 2.0 * np.power(current_radius, 2)
    neigh =  np.exp(-distances_from_winner / denominator)
    neigh = neigh.reshape(10,1)
    print("mmm" + str(neigh.shape))
    return neigh




def euclidean_dist(W, point):
    dst = np.sqrt((point[0] - W[:,0]) ** 2 + (point[1] - W[:,1]) ** 2)
    return dst

# Updating weights:
# delta weights = current learning rate * neighborhood parameter * actual distance from data point
def update_location(W, data_point, winning_idx, radius, alpha):
    # ed = euclidean_dist(W, data_point)
    print("inside update locations")
    for node_idx in range(W.shape[0]):
        if abs(winning_idx-node_idx) < radius:
            print("inside radius")
            W[node_idx] += alpha * (data_point - W[node_idx])
            print("after update locations")
    return W

def kohonen():
    data_container = np.zeros((number_iteration,2))
    time = 0
    W = initialize()
    for epoch in range(number_iteration):
        time += 1
        if epoch < max_time_learning_rate_update:
            current_learning_rate = learning_rate(time)
            current_radius = radius(time)
        else:
            current_learning_rate = 0.2
            current_radius = 1.0
        data_point = np.random.uniform(low = 0.0, high = 1.0, size = 2)
        data_container[epoch] = data_point
        closest_neuron_index = winning_neuron(W, data_point)
        W = update_location(W, data_point, closest_neuron_index, current_radius, current_learning_rate)
        print("after new wehigts")
        # draw:
        print("wtf")
        plt.clf()
        print("data_container.shape[0] = " + str(data_container.shape[0]))
        for i in range(data_container.shape[0]):
            print("after new wehigts")
            plt.scatter(data_container[i, 0], data_container[i, 1], color="green", s=30)
        for i in range(W.shape[0]):
            plt.scatter(W[i, 0], W[i, 1], color="blue", s=30)
        plt.plot(W[:, 0], W[:, 1], color='green', linewidth=1)
        plt.pause(0.05)
        plt.xlabel('x - axis')
        # frequency label
        plt.ylabel('y - axis')
        # plot title
        plt.title('Points')
        # showing legend
        if epoch % 10 == 0:
            print("epoch: " + str(epoch))
            print("W: \n" + str(W))

    # draw(W,data_container)
    plt.show()


kohonen()

