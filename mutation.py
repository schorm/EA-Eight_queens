"""
My colleciton of mutation methods

Student number:20311294 
Student name:Jing Tao
"""

# imports
import random

def permutation_swap (individual):
    """Mutate a permutation"""

    mutant = individual.copy()
    
    # student code starts
    select=random.sample(range(len(individual)),2)
    i=select[0]
    j=select[1]#get two random  allele
    mutant[i],mutant[j]=mutant[j],mutant[i]
    # student code ends
    
    return mutant
