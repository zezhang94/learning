package easy;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class BinaryNumberWithAlternatingBitsTest {

    @Test
    public void test() {
        BinaryNumberWithAlternatingBits f = new BinaryNumberWithAlternatingBits();
        assertEquals(false, f.hasAlternatingBits(17));
        assertEquals(true, f.hasAlternatingBits(5));
        assertEquals(false, f.hasAlternatingBits(6));
        assertEquals(false, f.hasAlternatingBits(7));
        assertEquals(false, f.hasAlternatingBits(11));
        assertEquals(true, f.hasAlternatingBits(10));
        assertEquals(true, f.hasAlternatingBits(0));
        assertEquals(true, f.hasAlternatingBits(1));
        assertEquals(true, f.hasAlternatingBits(2));
        assertEquals(false, f.hasAlternatingBits(3));
    }
}