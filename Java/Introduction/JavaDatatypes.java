import java.util.Scanner;

public class JavaDatatypes {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        for (int i = 0; i < N; i++) {
            try{
                long value = sc.nextLong();
            if (value >= Byte.MIN_VALUE && value <= Byte.MAX_VALUE) {
                System.out.println(value + " can be fitted in:");
                System.out.println("* byte");
                System.out.println("* short");
                System.out.println("* int");
                System.out.println("* long");
            } else if (value >= Short.MIN_VALUE && value <= Short.MAX_VALUE) {
                System.out.println(value + " can be fitted in:");
                System.out.println("* short");
                System.out.println("* int");
                System.out.println("* long");
            } else if (value >= Integer.MIN_VALUE && value <= Integer.MAX_VALUE) {
                System.out.println(value + " can be fitted in:");
                System.out.println("* int");
                System.out.println("* long");
            }
            else if (value >= Long.MIN_VALUE && value <= Long.MAX_VALUE) {
                System.out.println(value + " can be fitted in:");
                System.out.println("* long");
            }
            }
            catch (Exception e) {
                System.out.println(sc.next() + " can't be fitted anywhere.");
            }
        }
        sc.close();
    }
}
