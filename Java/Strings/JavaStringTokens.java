import java.util.Scanner;

public class JavaStringTokens {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine().trim();
        String[] words = s.split("[\\s!?,._'@]+");
        System.out.println(s.isEmpty() ? "0" : words.length);
        for (String word : words) {
            System.out.println(word);
        }
        scan.close();
    }
}
