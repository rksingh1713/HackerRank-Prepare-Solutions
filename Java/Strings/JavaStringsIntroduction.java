import java.util.Scanner;

public class JavaStringsIntroduction {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();
        sc.close();

        System.out.println(A.length() + B.length());

        System.out.println(A.compareTo(B) > 0 ? "Yes" : "No");

        System.out.print(String.valueOf(A.charAt(0)).toUpperCase() + A.substring(1, A.length()) + " "
                + String.valueOf(B.charAt(0)).toUpperCase() + B.substring(1, B.length()));
    }
}