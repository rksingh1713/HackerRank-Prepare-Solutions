import java.util.Scanner;

public class JavaStringReverse {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        sc.close();
        String rev = "";
        for (int i = 0; i < A.length(); i++) {
            rev += A.charAt(A.length() - i - 1);
        }
        System.out.println(A.equals(rev) ? "Yes" : "No");
    }
}