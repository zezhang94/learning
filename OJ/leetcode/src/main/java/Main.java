
import easy.MinimumIndexSumOfTwoLists;

/**
 * Main test.
 */
public class Main {

    public static void main(String[] args) {

        /*
        Combinations function = new Combinations();
        List<List<Integer>> result = function.combine(5, 3);
        for (List<Integer> list : result) {
            for (Integer item : list) {
                System.out.print(item + ", ");
            }
            System.out.println();
        }
        */

        MinimumIndexSumOfTwoLists f = new MinimumIndexSumOfTwoLists();
        String[] result = f.findRestaurant(
            new String[] {"Shogun", "Tapioca Express", "Burger King", "KFC"}, 
            new String[] {"Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"}
        );
    }
}