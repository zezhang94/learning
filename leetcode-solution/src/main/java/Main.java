import java.util.List;

import medium.Combinations;

/**
 * Main test.
 */
public class Main {

    public static void main(String[] args) {

        Combinations function = new Combinations();
        List<List<Integer>> result = function.combine(5, 3);
        for (List<Integer> list : result) {
            for (Integer item : list) {
                System.out.print(item + ", ");
            }
            System.out.println();
        }
    }
}