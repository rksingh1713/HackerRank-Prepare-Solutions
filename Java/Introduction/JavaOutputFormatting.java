import java.util.Scanner;

public class JavaOutputFormatting {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("================================");
        for (int i = 0; i < 3; i++) {
            String a = sc.next();
            int b = sc.nextInt();
            System.out.printf("%-15s%03d%n", a, b);
        }
        System.out.println("================================");
        sc.close();
    }
}
