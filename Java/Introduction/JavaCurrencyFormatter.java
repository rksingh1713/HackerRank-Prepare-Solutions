/* Doesn´t work in Java 15  */

import java.util.Locale;
import java.util.Scanner;
import java.text.NumberFormat;

public class JavaCurrencyFormatter {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Double payment = sc.nextDouble();
        sc.close();
        System.out.println("US: " + NumberFormat.getCurrencyInstance(Locale.US).format(payment));
        NumberFormat fmt = NumberFormat.getCurrencyInstance(new Locale("en", "IN"));
        System.out.println("India: " + fmt.format(payment));
        System.out.println("China: " + NumberFormat.getCurrencyInstance(Locale.CHINA).format(payment));
        System.out.println("France: " + NumberFormat.getCurrencyInstance(Locale.FRANCE).format(payment));
    }
}
