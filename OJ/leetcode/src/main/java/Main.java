import java.util.Arrays;

/**
 * Main test.
 */
public class Main {

    public static void main(String[] args) {
        DecodeWays_91 solution = new DecodeWays_91();

        System.out.println(solution.numDecodings("21"));
        System.out.println(solution.numDecodings("210"));
        System.out.println(solution.numDecodings("2101"));
        System.out.println(solution.numDecodings("301"));
        System.out.println(solution.numDecodings("27"));


    }

    private static void print(int[][] ans) {
        System.out.println("----------------");
        for (int[] line : ans) {
            System.out.println(Arrays.toString(line));
        }
    }

}