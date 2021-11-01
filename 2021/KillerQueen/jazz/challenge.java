import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

public class challenge {
    public static void main(String[] args) throws FileNotFoundException {
        int a;
        Scanner s = new Scanner(new BufferedReader(new FileReader("flag.txt")));
        String flag = s.nextLine();

        char[] r2 = flag.toCharArray();
        String build = "";
        for (a = 0; a < r2.length; ++a) {
            build = build + (char)(158 - r2[a]);
        }

        r2 = build.toCharArray();

        build = "";
        a = 0;
        while (2 * a < r2.length - 1) {
            build = build + (char)((2 * r2[2 * a] - r2[2 * a + 1] + 153) % 93 + 33);
            build = build + (char)((r2[2 * a + 1] - r2[2 * a] + 93) % 93 + 33);
            ++a;
        }

        System.out.println(build);
    }
}

