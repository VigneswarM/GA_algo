import random
import math
from Population import *
from itertools import combinations 
from _operator import pos

class Algorithm : 
    uniformRate = 0.5
    mutationRate = 0.1
    tournamentSize = 5
    elitism = True
    elitismOffset =0
    mutation =1
    index=1
    
    
    def __init__(self):
        self.elitism=True
        self.mutation=1
        self.index =1
        
    # Crossover individuals
    def crossover(self,indiv1,indiv2,newPopulation):
        print("Crossover Between and index : ",indiv1,indiv2)
        position =random.randint(0,3)
        cross1 = indiv2[:position] +indiv1[position:]
        cross2 = indiv1[:position] +indiv2[position:]
        print("After Crossover at positon",position,cross1,cross2)
        print("-----------------------------------------------")
        #mutation
        mutate1 = self.mutate(cross1)
        mutate2 = self.mutate(cross2)
        #adding new population
        newPopulation.save_individual(self.index,mutate1)
        newPopulation.save_individual(self.index+1,mutate2)
        self.index +=1
        
    
    #Mutate an individual
    def mutate(self,cross):
        if(random.randint(0,10)== self.mutation):
            position =random.randint(0,3)
            print("mutation positive at position",position,cross)
            if(cross[position]=='1'):
                cross[position]='0'
            else:
                cross[position]='1'
        print("After Mutation ",cross)
        print("-----------------------------------------------")
        return cross
            
            
            
    
       
    def evolve_Population(self,myPop):
        
        newPopulation = Population(myPop.get_size(),False,"2")
        #Saving the most fittest from old population
        newPopulation.save_individual(0,myPop.get_Fittest())
        print(newPopulation.individuals)
        #selecting two random individual
        crossover_List = list(combinations(Population.individuals, 2))
        
        #checking crossover probability and generating cross over population
        for pair in crossover_List: 
            i=1
            test = random.randint(0,100)
            if(test<=75):
                print("CrossOVer positive")
                (indiv1, indiv2) = pair
                self.crossover(indiv1,indiv2,newPopulation)
                i +=1   
        
        print("Generation 1 :")
        print(newPopulation.individuals,len(newPopulation.individuals))
        #removing Duplicates using dictionary
        print(newPopulation.dict_pop,len(newPopulation.dict_pop))
        print(newPopulation.dict_fitness,len(newPopulation.dict_fitness))
        print(newPopulation.get_Fittest())
        
        #selection of fittest based on population size
        
        
        
    
    
    
                
                
    
    