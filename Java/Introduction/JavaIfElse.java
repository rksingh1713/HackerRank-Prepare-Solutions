import java.io.IOException;
import java.util.Scanner;

public class JavaIfElse {
    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();

        if (N % 2 == 1) {
            System.out.println("Weird");
        } else {
            if (N >= 2 && N <= 5) {
                System.out.println("Not Weird");
            } else if (N >= 6 && N <= 20) {
                System.out.println("Weird");
            } else if (N >= 20) {
                System.out.println("Not Weird");

            }
        }

        scanner.close();
    }
}
