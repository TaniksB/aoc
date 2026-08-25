import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;

public class day3 {
    public static ArrayList<vector2> getPath (String[] wire) {
        var wirePath = new ArrayList<vector2>();
        char dir;
        String distStr;
        int dist;
        int currX = 0;
        int currY = 0;
        int age = 0;
        for (String move : wire) {
            dir = move.charAt(0);
            distStr = move.substring(1);
            dist = Integer.parseInt(distStr);
            for (int i = 0; i < dist; i++) {
                switch (dir) {
                    case 'U':
                        currY++;
                        break;
                    case 'D':
                        currY--;
                        break;
                    case 'R':
                        currX++;
                        break;
                    case 'L':
                        currX--;
                        break;
                }
                age++;
                var pos = new vector2(currX, currY, age);
                wirePath.add(pos);
            }
        }
        return wirePath;
    }

    public static void main(String[] args) throws IOException {
        Path inputPath = Path.of("input_3.txt");
        String input = Files.readString(inputPath);
        String[] wires = input.split("/");
        String[] firstMoves = wires[0].split(",");
        String[] secondMoves = wires[1].split(",");
        var firstWire = getPath(firstMoves);
        var secondWire = getPath(secondMoves);
        vector2 closest = new vector2(99999999, 99999999, 0);
        int earliest = 99999999;
        for (vector2 pos1 : firstWire) {
            for (vector2 pos2 : secondWire) {
                if (pos1.x == pos2.x && pos1.y == pos2.y) {
                    if (pos1.getMD() < closest.getMD()) {
                        closest = pos1;
                    }
                    if (pos1.age + pos2.age < earliest) {
                        earliest = pos1.age + pos2.age;
                    }
                }
            }
        }
        System.out.println("Par1 1: " + closest.getMD());
        System.out.println("Part 2: " + earliest);
    }
}
