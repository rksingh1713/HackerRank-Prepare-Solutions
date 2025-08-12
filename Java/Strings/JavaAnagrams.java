import java.util.Arrays;
import java.util.Scanner;

public class JavaAnagrams {

    static boolean isAnagram(String a, String b) {
        if (a.equals(b)) {
            return true;
        } else {
            char[] arr1 = a.toCharArray();
            char[] arr2 = b.toCharArray();
            Arrays.sort(arr1);
            Arrays.sort(arr2);
            return Arrays.equals(arr1, arr2);
        }

    }

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        String a = scan.next().toLowerCase();
        String b = scan.next().toLowerCase();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println((ret) ? "Anagrams" : "Not Anagrams");
    }
}
