import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;

public class test {
    public static void main(String[] args) throws IOException {
        Path inputPath = Path.of("");
        String input = Files.readString(inputPath);
        System.out.println(input);
    }
}