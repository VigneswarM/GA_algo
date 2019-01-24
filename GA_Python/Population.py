from Individual import *
import operator

class Population:
    
    individuals = []
    population_size =0
    fittest =0
    dict_fitness ={}
    dict_pop ={}
    
    #Create a population   
    def __init__(self,size,value,year):
        if(value):
            self.population_size = size
            print("creating Population of size",self.population_size,year)
            individual = Individual()
            if value:
                i=0
                while i < self.population_size:
                    indiv = individual.create_individual(year)
                    self.save_individual(i,indiv)
                    #self.generate_Fitness(i,indiv)
                    i += 1
                #print(self.dict_pop)
    
    #Get population size        
    def get_size(self):  
        return len(self.individuals) 
    
    #Getters
    def get_individuals(self, index):
        return self.individuals[index]
    
    #Save individual  
    def save_individual(self,index,value):
        print("Individual",index,value)
        self.individuals.insert(index, value)
        self.dict_pop[index] = value
        self.generate_Fitness(index,value)
        
        
        
    def generate_Fitness(self,index,value):
        self.dict_fitness[index] = FitnessCalculator.get_fitness(self,value)
            
       
    def get_Fittest(self):
        #print(self.dict_fitness)
        #3print(self.dict_pop)
        #print("--------------------------")
        #Finding the max fit function
        max_fittest = max(self.dict_fitness.items(), key=operator.itemgetter(1))[0]
        self.fittest = self.individuals[max_fittest]
        return self.fittest
        
        