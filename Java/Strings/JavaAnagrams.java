import java.util.Scanner;

public class Solution {
     static boolean isAnagram(String a, String b) {
        // If lengths differ, they can't be anagrams
        if (a.length() != b.length()) {
            return false;
        }

        // Convert both strings to lowercase
        a = a.toLowerCase();
        b = b.toLowerCase();

        // Frequency array for English alphabets (26 letters)
        int[] freq = new int[26];

        // Count characters from 'a'
        for (int i = 0; i < a.length(); i++) {
            freq[a.charAt(i) - 'a']++;
        }

        // Subtract counts using 'b'
        for (int i = 0; i < b.length(); i++) {
            freq[b.charAt(i) - 'a']--;
        }

        // If all counts are zero, they are anagrams
        for (int count : freq) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }


    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
