package easy;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

public class MinimumIndexSumOfTwoListsTest {

    @Test
    public void test() {
        MinimumIndexSumOfTwoLists f = new MinimumIndexSumOfTwoLists();
        
        assertArrayEquals(new String[] {"Shogun"}, f.findRestaurant(
                new String[] {"Shogun","Tapioca Express","Burger King","KFC"},
                new String[] {"Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"}
                )
        );

    }
    
}