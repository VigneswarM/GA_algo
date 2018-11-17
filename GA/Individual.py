import random
from FitnessCalculator import FitnessCalculator


class Individual:
    def __init__(self):
        self.gene_len = 4
        self.genes = []
        self.fitness = 0

    def create_individual(self,year):
        
        self.generate_gene()
        #Checking  Year constraints
        if(year == "1"):
            val = 0.5 * float(self.genes[0])+ 1.0* float(self.genes[1])+1.5 * float(self.genes[2])+0.1 * float(self.genes[3])
            if(val>3.1):
                self.create_individual("1")
        
        if(year == "2"):
            val = 0.3 * float(self.genes[0])+ 0.8* float(self.genes[1])+1.5 * float(self.genes[2])+0.4 * float(self.genes[3])
            if(val>2.5):
                self.create_individual("2")
                
        if(year == "3"):
            val = 0.2 * float(self.genes[0])+ 0.2* float(self.genes[1])+0.3 * float(self.genes[2])+0.1 * float(self.genes[3])
            if(val>0.4):
                self.create_individual("3")

        #print(self.genes)
        #return ''.join(self.genes)
        return self.genes
    
    
    def generate_gene(self):
        self.genes = []
        i = 0
        while i < self.gene_len:
            self.genes.append(''.join(str(random.randint(0, 1))))
            i += 1
        return self.gene_len
    
    def get_gene(self, index):
        return self.genes[index]

    def set_gene(self, index, value):
        print(index,value)
        self.genes[index] = value

    def get_fitness(self,value):
        if self.fitness == 0:
            self.fitness = FitnessCalculator.get_fitness(self, value)
        return self.fitness

