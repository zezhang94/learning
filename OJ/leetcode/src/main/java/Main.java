
import easy.MinimumIndexSumOfTwoLists;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * Main test.
 */
public class Main {

    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>(Arrays.asList(3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6));
        //Collections.shuffle(list);

        KthLargestElementInAnArray_215 f = new KthLargestElementInAnArray_215();
        int ans = f.findKthLargest(list.stream().mapToInt(i -> i).toArray(), list.size());
        System.out.println(ans);
    }
}