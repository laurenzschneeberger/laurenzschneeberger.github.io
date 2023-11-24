'''
A toy implementation of a 3-node Markov Chain
Laurenz Schneeberger | Salzburg, Austria | 24. Nov 2023
'''

import numpy as np
import pandas as pd


def transitions_matrix(node_1, node_2, node_3): 
    '''
    defines the transition matrix. each node_i should be a three-entry list. 
    1. first checks whether the passed lists define a valid transitions matrix. 
    2. then compiles a transitions matrix from the lists
    '''
    distributions = [node_1, node_2, node_3] 
    
    for j in  distributions: 
        enum1 = 0
        for i in j: 
            enum1 += i
        if enum1 > 1.02 or enum1 < 0.98 or len(j) != 3:
            print(f'{j} is not a valid node probability distribution')
            return None 
        
    transitions = pd.DataFrame([node_1, node_2, node_3])
    
    return transitions 

def simulate(transitions_matrix, steps=4): 
    '''
    runs through the transitions matrix n times. 
    '''
    initial = np.random.randint(0, 3)
    for j in range(steps): 
        distribution = {
                0: transitions_matrix.iloc[initial, 0],
                1: transitions_matrix.iloc[initial, 1],
                2: transitions_matrix.iloc[initial, 2]
            }
        states = list(distribution.keys())
        probabilities = list(distribution.values())
        sample = np.random.choice(states, p=probabilities, size=1)[0]
        initial = sample
        print(f' moved from {initial} -> {sample}')
    print(f'ended at {initial}')


# Run Code
x = [0, 0.5, 0.5]
y = [0.5, 0, 0.5]
z = [0.5, 0.5, 0]

tm = transitions_matrix(x, y, z)
simulate(tm)