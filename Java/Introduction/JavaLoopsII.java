import java.util.Scanner;

public class JavaLoopsII {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for (int i = 0; i < N; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int n = sc.nextInt();
            int temp = a;
            for (int j = 0; j < n; j++) {
                temp += (int) (Math.pow(2, j)) * b;
                System.out.print(temp + " ");
            }
            System.out.printf("\n");
        }
        sc.close();
    }
}
