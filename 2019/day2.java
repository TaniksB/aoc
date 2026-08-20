import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;
import java.util.ArrayList;

public class day2 {
    public static int compute(ArrayList<Integer> memory) {
        int pos = 0;
        int a;
        int b;
        int target;
        while (true) {
            a = memory.get(pos+1);
            b = memory.get(pos+2);
            target = memory.get(pos+3);
            switch (memory.get(pos)) {
                case 1:
                    memory.set(target, memory.get(a) + memory.get(b));
                    break;
                case 2:
                    memory.set(target, memory.get(a) * memory.get(b));
                    break;
                case 99:
                    return memory.get(0);
                default:
                    /*System.out.println("Something went wrong!");
                    System.exit(1);*/
                    return 0;
            }
            pos += 4;
        }
    }

    public static void main(String[] args) throws IOException {
        Path inputPath = Path.of("input_2.txt");
        String input = Files.readString(inputPath);
        String[] integersStr = input.split(",");
        var integers = new ArrayList<Integer>();
        for (String i : integersStr) {
            integers.add(Integer.parseInt(i));
        }
        int result;
        for (int noun = 0; noun < 100; noun++) {
            integers.set(1, noun);
            for (int verb = 0; verb < 100; verb++) {
                integers.set(2, verb);
                ArrayList<Integer> mem = new ArrayList<>(integers);
                result = compute(mem);
                //System.out.println("Attempting noun " + integers.get(1) + ", verb " + integers.get(2) + " result: " + result);
                if (result == 19690720) {
                    System.out.println("Answer: " + noun + verb);
                    System.exit(0);
                }
            }
        }
    }
}
