'''-----Imports-----'''
import numpy as np
import scipy.special
import random

#Nnet Class
class Nnet:

    #Initialize Nnet
    def __init__(self, num_input, num_hidden, num_output, weight_input_hidden=None, weight_hidden_output=None):
        self.num_input = num_input
        self.num_hidden = num_hidden
        self.num_output = num_output
        
        #Weights between input and hidden layer
        self.weight_input_hidden = np.random.uniform(-0.5,0.5, 
        size=(self.num_hidden, self.num_input))
        
        #Weights between hidden and output layer
        self.weight_hidden_output = np.random.uniform(-0.5,0.5,
        size=(self.num_output, self.num_hidden))
        
        #Activation function
        self.activation_function = lambda x: scipy.special.expit(x)
        print("weight_input_hidden: " +str(type(self.weight_input_hidden)))
        print("weight_hidden_output: " +str(type(self.weight_hidden_output)))
        
        #If we are loading a brain, load it
        if weight_input_hidden is not None and weight_hidden_output is not None:
            self.weight_input_hidden = weight_input_hidden 
            self.weight_hidden_output = weight_hidden_output

    '''Function which takes in inputs and returns the outputs of the neural network'''
    def get_outputs(self, inputs_list):
        inputs = np.array(inputs_list, ndmin=2).T
        #hidden layer inputs are the product of the inputs and weights
        hidden_inputs = np.dot(self.weight_input_hidden, inputs)
        #hidden layer outputs are the activation function values of the inputs
        hidden_outputs = self.activation_function(hidden_inputs)
        #those are the inputs to the output layer
        final_inputs = np.dot(self.weight_hidden_output, hidden_outputs)
        #the output layer outputs are the activation function values of the inputs we just calculated
        final_outputs = self.activation_function(final_inputs)
        #return the ouput layer activations
        return final_outputs

    '''Function which modifies the weights of the neural network'''
    def modify_weights(self):
        #run the weight arrays through the modify_array function, 'mutating' them
        Nnet.modify_array(self, self.weight_input_hidden)
        Nnet.modify_array(self, self.weight_hidden_output)

    '''Function which takes in 2 neural networks and mkes itself a new one which is a mix of the two'''
    def create_mixed_weights(self, nnet1, nnet2):
        self.weight_input_hidden = Nnet.get_mix_from_arrays(nnet1.weight_input_hidden,
        nnet2.weight_input_hidden)    
        self.weight_hidden_output = Nnet.get_mix_from_arrays(nnet1.weight_hidden_output,
        nnet2.weight_hidden_output)

    '''Function which takes in an array and randomly modifies it'''
    def modify_array(self, a):
        #iterate through the array, with read/write access
        for x in np.nditer(a, op_flags=['readwrite']):
            #Randomly, 20% of the time, 'mutate' the value
            if random.random() < 0.20:
                x[...] = np.random.random_sample() - 0.5

    '''combines the weights of the two neural networks'''
    def get_mix_from_arrays(ar1, ar2):
        total_entries = ar1.size 
        num_rows = ar1.shape[0]
        num_cols = ar1.shape[1]
        
        num_to_take = total_entries - int(total_entries * 0.5)
        #idx is an array of random indices to take for mixing
        idx = np.random.choice(np.arange(total_entries), num_to_take, replace=False)

        res = np.random.rand(num_rows, num_cols)
        for row in range(0, num_rows):
            for col in range(0, num_cols):
                index = row * num_cols + col
                if index in idx:
                    res[row][col] = ar1[row][col]
                else:
                    res[row][col] = ar2[row][col]
        return res