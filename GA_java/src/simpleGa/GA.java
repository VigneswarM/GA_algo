package simpleGa;

public class GA {

    public static void main(String[] args) {

        // Set a candidate solution
        FitnessCalc.setSolution("1111");

        // Create an initial population
        Population myPop = new Population(3, true);
        
        // Evolve our population until we reach an optimum solution
        int generationCount = 0;
        //System.out.println(myPop.getFittest().getFitness()+"   "+FitnessCalc.getMaxFitness());
        while (myPop.getFittest().getFitness() < FitnessCalc.getMaxFitness()) {
            generationCount++;
            System.out.println("Generation: " + generationCount + " Fittest: " + myPop.getFittest().getFitness());
            myPop = Algorithm.evolvePopulation(myPop);
        }
        System.out.println("Solution found!");
        System.out.println("Generation: " + generationCount);
        System.out.println("Genes:");
        System.out.println(myPop.getFittest());

    }
}