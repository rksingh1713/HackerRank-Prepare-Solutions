import java.util.Scanner;

public class JavaSubArray {

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int arraySize = scan.nextInt();

    int[] array = new int[arraySize];

    for (int i = 0; i < array.length; i++) {
      array[i] = scan.nextInt();
    }

    scan.close();

    int count = 0;

    for (int i = 0; i < array.length; i++) {
      int sum = 0;
      for (int j = i; j < array.length; j++) {
        sum += array[j];
        if (sum < 0) {
          count++;
        }
      }
    }

    System.out.println(count);
  }
}
