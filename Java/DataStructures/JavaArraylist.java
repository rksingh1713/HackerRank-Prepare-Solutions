import java.util.ArrayList;
import java.util.Scanner;

public class JavaArraylist {

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int lines = scan.nextInt();

    ArrayList<int[]> list = new ArrayList<>();

    for (int i = 0; i < lines; i++) {
      int[] array = new int[scan.nextInt()];
      for (int j = 0; j < array.length; j++) {
        array[j] = scan.nextInt();
      }
      list.add(array);
    }

    int queriesLength = scan.nextInt();

    int[][] queries = new int[queriesLength][2];

    for (int i = 0; i < queries.length; i++) {
      queries[i][0] = scan.nextInt();
      queries[i][1] = scan.nextInt();
    }
    scan.close();

    for (int i = 0; i < queries.length; i++) {
      if (
        (queries[i][0] - 1) < 0 ||
        (queries[i][0] - 1) >= list.size() ||
        (queries[i][1] - 1) >= list.get(queries[i][0] - 1).length ||
        list.get(queries[i][0] - 1).length == 0
      ) {
        System.out.println("ERROR!");
      } else {
        System.out.println(list.get((queries[i][0]) - 1)[(queries[i][1]) - 1]);
      }
    }
  }
}
