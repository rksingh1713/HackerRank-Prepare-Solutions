import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class JavaList {

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

    int n = scan.nextInt();

    List<Integer> list = new ArrayList<>();

    for (int i = 0; i < n; i++) {
      list.add(scan.nextInt());
    }

    int q = scan.nextInt();

    for (int i = 0; i < q; i++) {
      String operation = scan.next();
      if (operation.equals("Insert")) {
        int index = scan.nextInt();
        int value = scan.nextInt();
        list.add(index, value);
      } else if (operation.equals("Delete")) {
        int index = scan.nextInt();
        list.remove(index);
      }
    }

    scan.close();

    String result = String.join(
      " ",
      list.stream().map(String::valueOf).collect(Collectors.toList())
    );
    System.out.println(result);
  }
}
