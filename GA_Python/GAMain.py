from Individual import Individual
from Population import  *
from Algorithm import * 




def __init__(self):
    generation_count=0
    
  
   

def main():
    print("GA started!")
    year ="1"
    fitnessCalc = FitnessCalculator()
    algo = Algorithm()
    fitnessCalc.setsolution("1111")
    myPop = Population(3,True,year)
    generation_count =0
    #myPop.generate_Fitness()
    val =myPop.get_Fittest()
    print("Fittest : " ,val)
    generation_count += 1       
    print("Generation: ", generation_count, " Fittest: " , fitnessCalc.get_fitness(val))
    print("-------Starting generations : ",generation_count," ------------------")
    myPop= algo.evolve_Population(myPop) 
    #print("Solution found!")
    #print("Generation: %-10s" % (generation_count))
    #print("Genes:");
    #print(myPop.get_Fittest())      
    
    
    

if __name__=='__main__':
    main()
