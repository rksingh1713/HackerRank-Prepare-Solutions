import java.text.NumberFormat;
import java.util.Locale;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double payment = sc.nextDouble();
        sc.close();

        // Format for US
        String us = NumberFormat.getCurrencyInstance(Locale.US).format(payment);
        
        // Format for India (Java doesn't have predefined Locale for India)
        String india = NumberFormat.getCurrencyInstance(new Locale("en", "IN")).format(payment);
        
        // Format for China
        String china = NumberFormat.getCurrencyInstance(Locale.CHINA).format(payment);
        
        // Format for France
        String france = NumberFormat.getCurrencyInstance(Locale.FRANCE).format(payment);

        // Print in the expected format
        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
