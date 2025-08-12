import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Java1DArrayPart2 {

  public static boolean canWin(int leap, int[] game) {
    int i = 0;
    Queue<Integer> list = new LinkedList<>();
    list.add(leap);
    list.add(i + 1);
    while (!list.isEmpty()) {
      int next = list.poll();
      if (next > game.length - 1) return true;
      if (game[next] == 0) {
        i = next;
        if (i != 0) list.add(i - 1);
        list.add(i + leap);
        list.add(i + 1);
        game[i] = 1;
      }
    }
    return false;
  }

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int q = scan.nextInt();
    while (q-- > 0) {
      int n = scan.nextInt();
      int leap = scan.nextInt();

      int[] game = new int[n];
      for (int i = 0; i < n; i++) {
        game[i] = scan.nextInt();
      }

      System.out.println((canWin(leap, game)) ? "YES" : "NO");
    }
    scan.close();
  }
}
