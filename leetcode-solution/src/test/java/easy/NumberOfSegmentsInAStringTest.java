package easy;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/**
 * NumberOfSegmentsInAStringTest
 */
public class NumberOfSegmentsInAStringTest {

    @Test
    void check() {
        NumberOfSegmentsInAString function = new NumberOfSegmentsInAString();
        assertEquals(5, function.countSegments("Hello, my name is John"));
        assertEquals(0, function.countSegments("                "));
    }
}