import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class TagContentExtractor {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());
        Boolean isExist = false;
        while (testCases > 0) {
            isExist = false;
            String line = in.nextLine();

            String regex = "<([^<>]+)>([^<>]+)<\\/\\1>";
            Pattern p = Pattern.compile(regex);

            Matcher m = p.matcher(line);

            while (m.find()) {
                String validString = m.group(2);
                if (!validString.isEmpty()) {

                    System.out.println(validString);
                } else {
                    System.out.println("None");
                }
                isExist = true;
            }

            if (isExist == false) {
                System.out.println("None");
            }

            testCases--;
        }
        in.close();
    }
}
