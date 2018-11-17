import math


class FitnessCalculator:

  
    solution = []
    
    def __init__(self):
        print(" ")
        self.solution=[]

    def get_fitness_value(self, individual):
        print("Get fitness for :: ", individual)
        
    # Set a candidate solution
    def set_solution(self,newsolution =[]):
        self.solution = newsolution
    
    # use this method to set our candidate solution with string of 0s and 1s
    def setsolution(self,newsolution):
        print("Setting fitness solution", newsolution)
        i=0
        while i < len(newsolution):
            char = newsolution[i]
            if((char == "0") or (char == "1")):
                self.solution.append(char)
                #print(self.solution)
            else:
                self.solution.append('0') 
                #print(self.solution)
            i +=1
            
            
    def get_fitness(self,individual):
        fitness = 0.2 * float(individual[0]) + 0.3 * float(individual[1]) + 0.5 * float(individual[2])+0.1 * float(individual[3])
        #print("Fitness value of : ",individual,fitness)
        return fitness
                
    def get_maxfitness(self):
        maxFitness = 0.2*float(self.solution[0])+0.3*float(self.solution[1])+0.5*float(self.solution[2])+0.1*float(self.solution[3])   
        return maxFitness     
                
                
            
        
