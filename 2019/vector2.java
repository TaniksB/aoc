public class vector2 {
    public int x;
    public int y;
    public int age;
    public vector2(int newX, int newY, int newAge) {
        x = newX;
        y = newY;
        age = newAge;

    }

    public int getMD() {
        return Math.abs(x) + Math.abs(y);
    }
}
