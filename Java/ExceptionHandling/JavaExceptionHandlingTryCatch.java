import java.util.InputMismatchException;
import java.util.Scanner;

public class JavaExceptionHandlingTryCatch {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    try {
      int x = sc.nextInt();
      int y = sc.nextInt();
      sc.close();
      System.out.println(x / y);
    } catch (InputMismatchException e) {
      System.out.println("java.util.InputMismatchException");
    } catch (ArithmeticException e) {
      System.out.println(e);
    } catch (Exception e) {
      System.out.println(e);
    }
  }
}
