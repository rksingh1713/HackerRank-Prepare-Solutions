import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class JavaRegex {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Pattern pat = Pattern.compile(MyRegex.regex);
        while (in.hasNext()) {
            Matcher mat = pat.matcher(in.nextLine());
            System.out.println(mat.find() ? "true" : "false");
        }
        in.close();
    }
}

class MyRegex {
    static String regex = "^(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\\."
            + "(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\\."
            + "(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})\\."
            + "(25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})$";
}
