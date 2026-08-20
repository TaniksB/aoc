import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;

public class day1 {
    public static void main(String[] args) throws IOException {
        Path inputPath = Path.of("input_1.txt");
        String input = Files.readString(inputPath);
        String[] modules = input.split("\n");

        int fuelTotal = 0;
        
        for (String module : modules) {
            int moduleInt = Integer.parseInt(module);
            int fuelReq = 1;
            while (fuelReq > 0) {
                fuelReq = Math.floorDiv(moduleInt, 3) - 2;
                if (fuelReq > 0) {fuelTotal += fuelReq;}
                // String debug = "logged ";
                // debug += fuelReq;
                // System.out.println(debug);
                moduleInt = fuelReq;
            }
            
        }

        System.out.println("Total fuel requirement is:");
        System.out.println(fuelTotal);

    }
}