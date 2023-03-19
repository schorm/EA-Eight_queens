"""
My collection of initialization methods for different representations

Student number:20311294 
Student name:Jing Tao
"""

#imports
import random

def permutation (pop_size, chrom_length):
    """initialize a population of permutation"""

    population = []
    # student code begin
    for _ in range(pop_size):
        chrom=list(range(0,8))
        random.shuffle(chrom)
        population.append(chrom)
    #student code end
    return population                     
 
