import java.util.BitSet;
import java.util.Scanner;

public class JavaBitSet {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int m = scanner.nextInt();
    scanner.nextLine();

    BitSet bit1 = new BitSet(n);
    BitSet bit2 = new BitSet(n);

    for (int i = 0; i < m; i++) {
      String line = scanner.nextLine();
      Scanner inputScan = new Scanner(line);

      String command = inputScan.next();
      int B1 = inputScan.nextInt();
      int B2 = inputScan.nextInt();

      switch (command) {
        case "AND":
          if (B1 == 1) {
            bit1.and(bit2);
          } else {
            bit2.and(bit1);
          }
          break;
        case "OR":
          if (B1 == 1) {
            bit1.or(bit2);
          } else {
            bit2.or(bit1);
          }
          break;
        case "XOR":
          if (B1 == 1) {
            bit1.xor(bit2);
          } else {
            bit2.xor(bit1);
          }
          break;
        case "SET":
          if (B1 == 1) {
            bit1.set(B2);
          } else {
            bit2.set(B2);
          }
          break;
        case "FLIP":
          if (B1 == 1) {
            bit1.flip(B2);
          } else {
            bit2.flip(B2);
          }
          break;
      }

      System.out.println(bit1.cardinality() + " " + bit2.cardinality());
      inputScan.close();
    }

    scanner.close();
  }
}
