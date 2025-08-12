
import java.util.Scanner;
import java.util.Stack;

public class JavaStack {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    while (sc.hasNext()) {
      String input = sc.next();
      System.out.println(isBalanced(input));
    }
    sc.close();
  }

  private static Boolean isBalanced(String input) {
    Stack<Character> stack = new Stack<>();
    for (char c : input.toCharArray()) {
      if (c == '(' || c == '[' || c == '{') {
        stack.push(c);
      } else if (c == ')' && !stack.isEmpty() && stack.peek() == '(') {
        stack.pop();
      } else if (c == ']' && !stack.isEmpty() && stack.peek() == '[') {
        stack.pop();
      } else if (c == '}' && !stack.isEmpty() && stack.peek() == '{') {
        stack.pop();
      } else {
        return false;
      }
    }
    return stack.isEmpty();
  }
}
