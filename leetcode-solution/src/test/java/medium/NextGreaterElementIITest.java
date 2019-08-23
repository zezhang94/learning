package medium;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

public class NextGreaterElementIITest {

    @Test
    public void test() {
        NextGreaterElementII f = new NextGreaterElementII();
        assertArrayEquals(new int[] {2, -1, 2}, f.nextGreaterElements(new int[] {1, 2, 1}));
    }
}