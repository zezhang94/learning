package easy;

import java.util.Arrays;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * # 599
 * Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
 * You need to help them find out their common interest with the least list index sum. 
 * If there is a choice tie between answers, output all of them with no order requirement. 
 * You could assume there always exists an answer.
 * 
 * Example 1:
 *  Input:
 *  ["Shogun", "Tapioca Express", "Burger King", "KFC"]
 *  ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
 *  Output: ["Shogun"]
 *  Explanation: The only restaurant they both like is "Shogun".
 * 
 * Example 2:
 *  Input:
 *  ["Shogun", "Tapioca Express", "Burger King", "KFC"]
 *  ["KFC", "Shogun", "Burger King"]
 *  Output: ["Shogun"]
 *  Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
 * 
 * Note:
 *  The length of both lists will be in the range of [1, 1000].
 *  The length of strings in both lists will be in the range of [1, 30].
 *  The index is starting from 0 to the list length minus 1.
 *  No duplicates in both lists.
 */
public class MinimumIndexSumOfTwoLists {

    public String[] findRestaurant(String[] list1, String[] list2) {

        LinkedList<String> resultList = new LinkedList<>();
        
        Map<String, Integer> map = new HashMap<>();
        String[] list = list1.length < list2.length ? list1 : list2;
        for (int i = 0; i < list.length; i++) {
            map.put(list[i], i);
        }

        list = list1.length >= list2.length ? list1 : list2;
        int min = list1.length + list2.length - 2;
        Integer temp;
        for (int i = 0; i < list.length; i++) {
            temp = map.get(list[i]);
            if (null != temp) {
                if (temp + i < min) {
                    resultList.clear();
                    resultList.add(list[i]);
                    min = temp + i;
                } else if (temp + i == min) {
                    resultList.add(list[i]);
                }
            }
        }

        return resultList.toArray(new String[resultList.size()]);
    
    }
}