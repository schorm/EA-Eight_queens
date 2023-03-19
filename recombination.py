"""
My collection of recombination methods

Student number:20311294 
Student name:Jing Tao
"""

#imports
import random

def permutation_cut_and_crossfill (parent1, parent2):
    """cut-and-crossfill crossover for permutation representations"""

    offspring1 = []
    offspring2 = []
    # student code begin
    # get the random cut point
    point=random.randint(0,len(parent1)-1)
    left_off1=parent1[:point]
    right_off1=parent1[point:]
    
    offspring1=left_off1.copy()
    left_off2=parent2[:point]
    right_off2=parent2[point:]
    offspring2=left_off2.copy()

    #cut_and_crossfill parent2 to parent1
    for right_val2 in right_off2:
        if(not (right_val2 in offspring1)):
            offspring1.append(right_val2)
    for left_val2 in left_off2:
        if(not left_val2 in offspring1):
            offspring1.append(left_val2)

    # cut_and_crossfill parent1 to parent2
    for right_val1 in right_off1:
        if(not (right_val1 in offspring2)):
            offspring2.append(right_val1)
    for left_val1 in left_off1:
        if(not(left_val1 in offspring2)):
            offspring2.append(left_val1)
    # student code end 

    return offspring1, offspring2
