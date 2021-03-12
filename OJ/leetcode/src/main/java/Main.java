import java.util.Arrays;

/**
 * Main test.
 */
public class Main {
    public static void main(String[] args) {
        DifferentWaysToAddParentheses_241 solution = new DifferentWaysToAddParentheses_241();

        System.out.println(solution.diffWaysToCompute("2-1-1").toString());
        System.out.println(solution.diffWaysToCompute("2*3-4*5").toString());
        System.out.println(solution.diffWaysToCompute("0").toString());

    }

    private static void print(int[][] ans) {
        System.out.println("----------------");
        for (int[] line : ans) {
            System.out.println(Arrays.toString(line));
        }
    }
}