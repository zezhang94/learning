package medium;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class ArrayOfDoubledPairsTest {

    @Test
    public void test() {
        ArrayOfDoubledPairs function = new ArrayOfDoubledPairs();
        assertTrue(function.canReorderDoubled(new int[]{2,1,2,1,1,1,2,2}));
        assertTrue(function.canReorderDoubled(new int[]{4,-2,2,-4}));
        assertFalse(function.canReorderDoubled(new int[]{3,1,3,6}));
        assertFalse(function.canReorderDoubled(new int[]{2,1,2,6}));
        assertFalse(function.canReorderDoubled(new int[]{1,2,4,16,8,4}));
    }
}