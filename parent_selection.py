"""
My collection of parent selection methods

Student number:20311294 
Student name:Jing Tao
"""

# imports
import random



def MPS(fitness, mating_pool_size):
    """Multi-pointer selection (MPS)"""

    selected_to_mate = []

    # student code starts
    #make the cumulative probability distribution 
    parents=[0]*mating_pool_size
    a=[]
    for i in range(len(fitness)):
        a.append(fitness[i]/sum(fitness))
    for j in range(1,len(a)):
        a[j]+=a[j-1]
    #selection
    current_number=0
    i=0
    r=random.uniform(0,1/mating_pool_size)
    while(current_number<mating_pool_size):
        while(r<=a[i]):       
            parents[current_number]=fitness[i]
            r=r+1/mating_pool_size
            current_number+=1
        i+=1
    #get the selected parents index    
    for value in parents:
        selected_to_mate.append(fitness.index(value))
    # student code ends
    
    return selected_to_mate


def tournament(fitness, mating_pool_size, tournament_size):
    """Tournament selection without replacement"""

    selected_to_mate = []

    # student code starts
    parents=[]
    current_number=0
    while(current_number<mating_pool_size):
        random_individual=random.sample(fitness,tournament_size)
        i=max(random_individual)
        parents.append(i)
        current_number+=1

    #get the selected parents index    
    for value in parents:
        selected_to_mate.append(fitness.index(value))
    # student code ends
    
    return selected_to_mate


def random_uniform (population_size, mating_pool_size):
    """Random uniform selection"""

    selected_to_mate = []

    # student code starts
    selected_to_mate=random.sample(range(population_size),mating_pool_size)

    # student code ends
    
    return selected_to_mate

