import java.security.MessageDigest;
import java.util.Scanner;

public class JavaMD5 {

  public static void main(String[] args) {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    Scanner sc = new Scanner(System.in);
    String input = sc.nextLine();
    sc.close();
    try {
      MessageDigest md5 = MessageDigest.getInstance("MD5");
      md5.update(input.getBytes());
      byte[] digest = md5.digest();

      StringBuilder sb = new StringBuilder();
      for (byte b : digest) {
        //converting byte to hexadecimal
        sb.append(String.format("%02x", b));
      }
      System.out.println(sb.toString());
    } catch (Exception e) {
      System.out.println(e);
    }
  }
}
