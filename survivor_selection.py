"""
My collection of survivor selection methods

Student number:20311294 
Student name:Jing Tao
"""

#imports
import random


def mu_plus_lambda(current_pop, current_fitness, offspring, offspring_fitness):
    """mu+lambda selection"""
    population = []
    fitness = []

    # student code starts
    mu=len(current_pop)
    pop=current_pop+offspring
    fit=current_fitness+offspring_fitness
    pop = [x for _, x in sorted(zip(fit, pop), key=lambda pair: pair[0], reverse=True)]    
    fit.sort(reverse=True)
    population=pop[:mu]
    fitness=fit[:mu]
    # student code ends
    
    return population, fitness


def replacement(current_pop, current_fitness, offspring, offspring_fitness):
    """replacement selection"""

    population = []
    fitness = []

    # student code starts
    lambd=len(offspring)
    pop = [x for _, x in sorted(zip(current_fitness, current_pop), key=lambda pair: pair[0], reverse=True)]    
    pop_fit=current_fitness
    pop_fit.sort(reverse=True)
    population=pop[:len(pop)-lambd]+offspring
    fitness=pop_fit[:len(pop)-lambd]+offspring_fitness
    # student code ends
    
    return population, fitness


def random_uniform(current_pop, current_fitness, offspring, offspring_fitness):
    """random uniform selection"""
    population = []
    fitness = []

    
    # student code starts
    pop=current_pop+offspring
    fit=current_fitness+offspring_fitness
    random_index=random.sample(range(len(pop)),len(current_pop))
    population = [pop[i] for i in random_index]
    fitness=[fit[i] for i in random_index]
    # student code ends
    
    return population, fitness


