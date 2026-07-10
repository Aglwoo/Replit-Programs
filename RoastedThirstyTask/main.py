import numpy as np

# Define training data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input data
Y = np.array([[0], [1], [1], [0]])  # Output data

# Define and train the model
input_dim = X.shape[1]
hidden_dim = 3
output_dim = Y.shape[1]

# Initialize weights randomly
np.random.seed(1)
synapse_0 = 2 * np.random.random((input_dim, hidden_dim)) - 1
synapse_1 = 2 * np.random.random((hidden_dim, output_dim)) - 1

# Train the model
epochs = 10000
learning_rate = 0.1
for epoch in range(epochs):
    # Forward propagation
    layer_0 = X
    layer_1 = 1 / (1 + np.exp(-(np.dot(layer_0, synapse_0))))
    layer_2 = 1 / (1 + np.exp(-(np.dot(layer_1, synapse_1))))

    # Back propagation
    layer_2_error = Y - layer_2
    layer_2_delta = layer_2_error * (layer_2 * (1 - layer_2))
    layer_1_error = layer_2_delta.dot(synapse_1.T)
    layer_1_delta = layer_1_error * (layer_1 * (1 - layer_1))

    # Update weights
    synapse_1 += learning_rate * layer_1.T.dot(layer_2_delta)
    synapse_0 += learning_rate * layer_0.T.dot(layer_1_delta)

# Test the model
test_input = np.array([[0, 1]])
layer_0 = test_input
layer_1 = 1 / (1 + np.exp(-(np.dot(layer_0, synapse_0))))
layer_2 = 1 / (1 + np.exp(-(np.dot(layer_1, synapse_1))))
print(layer_2)  # Print the output