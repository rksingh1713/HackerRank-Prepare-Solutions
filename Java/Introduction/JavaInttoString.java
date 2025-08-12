import java.util.Scanner;

public class JavaInttoString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        String s = Integer.toString(n);
        if (s instanceof String) {
            System.out.println("Good job");
        }
        else {
            System.out.println("Wrong answer");
        }

    }
}