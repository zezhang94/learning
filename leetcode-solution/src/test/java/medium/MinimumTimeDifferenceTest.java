package medium;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;

import org.junit.jupiter.api.Test;

public class MinimumTimeDifferenceTest {

    @Test
    public void check() {
        MinimumTimeDifference f = new MinimumTimeDifference();
        assertEquals(1, f.findMinDifference(Arrays.asList("23:59","00:00")));
        assertEquals(147, f.findMinDifference(Arrays.asList("05:31","22:08","00:35")));
    }    
}