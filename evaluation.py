"""
My collection of fitness evaluation methods

Student number:20311294 
Student name:Jing Tao
"""

#imports


def fitness_8queen (individual): 
    """Compute fitness of an invidual for the 8-queen puzzle (maximization)"""    

    fitness = 0
    # student code begin
    #individual=population[i]
    ind_length=len(individual)
    for i in range(ind_length):
        for j in range (i+1,ind_length):
            if individual[i]!=individual[j]:
                fitness+=1# if two queens are not in each row
            if abs(i-j)!=abs(individual[i]-individual[j]):
                fitness+=1# if two queens are not in diagonal


    # student code end
    
    return fitness


