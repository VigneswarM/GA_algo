package simpleGa;

public class FitnessCalc {

    static byte[] solution = new byte[4];

    /* Public methods */
    // Set a candidate solution as a byte array
    public static void setSolution(byte[] newSolution) {
        solution = newSolution;
    }

    // To make it easier we can use this method to set our candidate solution 
    // with string of 0s and 1s
    static void setSolution(String newSolution) {
        solution = new byte[newSolution.length()];
        // Loop through each character of our string and save it in our byte 
        // array
        for (int i = 0; i < newSolution.length(); i++) {
            String character = newSolution.substring(i, i + 1);
            if (character.contains("0") || character.contains("1")) {
                solution[i] = Byte.parseByte(character);
            } else {
                solution[i] = 0;
            }
        }
    }

    // Calculate individual fitness by comparing it to our candidate solution
    static double getFitness(Individual individual) {
        double fitness = 0;
//        // Loop through our individuals genes and compare them to our candidates
//        for (int i = 0; i < individual.size() && i < solution.length; i++) {
//            if (individual.getGene(i) == solution[i]) {
//                fitness++;
//            }
//        }
        //System.out.println(individual.getGene(0)+" "+individual.getGene(1)+" "+individual.getGene(2)+" "+individual.getGene(3));
        fitness = 0.2*(float)individual.getGene(0)+0.3*(float)individual.getGene(1)+0.5*(float)individual.getGene(2)+0.1*(float)individual.getGene(3);
        return fitness;
    }
    
    // Get optimum fitness
    static double getMaxFitness() {
        double maxFitness = 0.2*(float)solution[0]+0.3*(float)solution[1]+0.5*(float)solution[2]+0.1*(float)solution[3];
        return maxFitness;
    }
}