import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;

public class PatternSyntaxChecker {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int testCases = Integer.parseInt(in.nextLine());
		while (testCases > 0) {
			String pattern = in.nextLine();
			try {
				Pattern regex = Pattern.compile(pattern);
				if (regex != null) {
					System.out.println("Valid");
				} else {
					System.out.println("Invalid");
				}
			} catch (PatternSyntaxException e) {
				System.out.println("Invalid");
			}
			testCases--;
		}
		in.close();
	}
}
