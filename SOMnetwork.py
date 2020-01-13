import numpy as np
import random
# number of neurons in the pattern. in Question 1 case: a line with 100 neurons.
pattern_length = 10

# Time: increase with every new data point
time = 0
number_iteration = 10000
# After some time learning rate will converge to zero
max_time_learning_rate_update = 1500
time_constant = int(0.1 * number_iteration) # = TAU IN LECTURE
#
alpha_0 = 1.0 # = ETA IN LECTURE
alpha_infinte = 0.05
# initial radius: % of
init_rad = 50 # = SIGMA IN LECTURE








def initialize():
    # np.random.normal, size param =
    # Output shape. If the given shape is, e.g., (m, n, k), then m * n * k samples are drawn
    W = np.random.uniform(0, 1, size=pattern_length)
    return W

def winning_neuron(W, data_point):
    distances = np.array(W - data_point)
    winnig_unit = np.argmin(distances) # index of the min distance
    return winnig_unit

def update_location(max_activation_unit):

    return

# This learning rate indicates how much we want to adjust our weights.
# After time max_time_learning_rate_update (positive infinite), this learning rate will converge to zero
# so we will have no update even for the neuron winner .
def learning_rate():
    return alpha_0 * np.exp(-float(t) / tau)


def kohonen():
    W = initialize()
    for t in range(number_iteration):
        data_point = random.random(0,1)
        winning_neuron(W, data_point)
        update_location()



w = initialize()
print(w)
data_point = 0.1
distances = np.array(w - data_point)
print(distances)
print(np.argmin(distances))
