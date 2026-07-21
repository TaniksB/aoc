import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;

public class test {
    public static void main(String[] args) throws IOException {
        Path inputPath = Path.of("input_2.txt");
        String input = Files.readString(inputPath);
        String[] Intcode_str = input.split(",");
        int[] Intcode = new int[Intcode_str.length];
        int counter = 0;
        for (String entry : Intcode_str) {
            Intcode[counter] = Integer.parseInt(entry);
            counter++;
        }
        int position = 0;
        while (1 > 0) {
            int opcode = Intcode[position];
            int a = Intcode[position+1];
            int b = Intcode[position+2];
            int target = Intcode[position+3];
            switch (opcode) {
                case 1:
                    Intcode[target] = Intcode[a] + Intcode[b];
                    break;
                case 2:
                    Intcode[target] = Intcode[a] * Intcode[b];
                    break;
                case 99:
                    System.out.println("The value at position 0 is:");
                    System.out.println(Intcode[0]);
                    System.exit(0);
                default:
                    System.out.println("Something went wrong!");
                    System.exit(0);
            }
            position += 4;
        }
    }
}
