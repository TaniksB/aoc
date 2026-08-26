import java.util.ArrayList;
import java.util.Objects;

public class day4 {
    public static boolean noDecrease(int inputInt) {
        var input = new ArrayList<Integer>();
        int digit;
        while (inputInt != 0) {
            digit = inputInt % 10;
            input.add(digit);
            inputInt -= digit;
            inputInt /= 10;
        }
        for (int left = 0; left < input.size()-1; left++) {
            if (input.get(left) < input.get(left+1)) {
                return false;
            }
        }
        return true;
    }

    public static boolean hasDouble(int inputInt) {
        var input = new ArrayList<Integer>();
        int digit;
        var doubles = new ArrayList<Integer>();
        var banned = new ArrayList<Integer>();
        while (inputInt != 0) {
            digit = inputInt % 10;
            input.add(digit);
            inputInt -= digit;
            inputInt /= 10;
        }
        for (int left = 0; left < input.size()-1; left++) {
            if (Objects.equals(input.get(left), input.get(left + 1))) {
                if (doubles.contains(input.get(left))) {
                    banned.add(input.get(left));
                } else {
                    doubles.add(input.get(left));
                }
            }
        }
        for (int i : doubles) {
            if (!banned.contains(i)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int valids = 0;
        for (int i = 134564; i <= 585159; i++) {
            if (noDecrease(i) && hasDouble(i)) {
                valids++;
            }
        }
        System.out.println("Part 2: " + valids);
    }
}
