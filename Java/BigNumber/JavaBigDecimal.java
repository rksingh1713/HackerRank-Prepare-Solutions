import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;
import java.math.BigDecimal;

public class JavaBigDecimal {
    public static void main(String[] args) {
        // Input
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] s = new String[n + 2];
        for (int i = 0; i < n; i++) {
            s[i] = sc.next();
        }
        sc.close();

        s = Arrays.copyOf(s, n);

        Arrays.sort(s, new Comparator<String>() {
            public int compare(String s1, String s2) {
                BigDecimal b1 = new BigDecimal(s1);
                BigDecimal b2 = new BigDecimal(s2);
                return b2.compareTo(b1);
            }
        });

        // Output
        for (int i = 0; i < n; i++) {
            System.out.println(s[i]);
        }
    }
}
