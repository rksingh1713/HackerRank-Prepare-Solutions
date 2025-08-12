import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class JavaComparator {

  static class Player {

    String name;
    int score;

    Player(String n, int s) {
      this.name = n;
      this.score = s;
    }
  }

  static class Checker implements Comparator<Player> {

    @Override
    public int compare(Player a, Player b) {
      if (a.score != b.score) return b.score - a.score;
      return a.name.compareTo(b.name);
    }
  }

  public static class Solution {

    public static void main(String[] args) throws Exception {
      BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
      List<Player> a = new ArrayList<>();
      int n = Integer.parseInt(in.readLine());
      while (n != 0) {
        String[] p = in.readLine().split(" ");
        a.add(new Player(p[0], Integer.parseInt(p[1])));
        n -= 1;
      }
      Checker check = new Checker();
      a.sort(check);
      for (Player i : a) {
        System.out.println(i.name + " " + i.score);
      }
      in.close();
    }
  }
}
