

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashSet;
import java.util.Scanner;

public class JavaDequeue {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    Deque<Integer> deque = new ArrayDeque<>();
    int n = in.nextInt();
    int m = in.nextInt();
    int maxUnique = 0;
    HashSet<Integer> hashSet = new HashSet<>();

    for (int i = 0; i < n; i++) {
      int num = in.nextInt();
      deque.add(num);
      hashSet.add(num);
      if (deque.size() == m) {
        if (hashSet.size() > maxUnique) {
          maxUnique = hashSet.size();
        }
        int removed = deque.poll();

        if (!deque.contains(removed)) {
          hashSet.remove(removed);
        }
      }
    }
    in.close();
    System.out.println(maxUnique);
  }
}
