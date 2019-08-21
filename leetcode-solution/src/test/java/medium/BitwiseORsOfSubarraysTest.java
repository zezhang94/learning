package medium;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class BitwiseORsOfSubarraysTest {

    @Test
    public void test() {
        BitwiseORsOfSubarrays function = new BitwiseORsOfSubarrays();
        assertEquals(1, function.subarrayBitwiseORs(new int[] {0}));
        assertEquals(3, function.subarrayBitwiseORs(new int[] {1, 1, 2}));
        assertEquals(6, function.subarrayBitwiseORs(new int[] {1, 2, 4}));
    }
}
