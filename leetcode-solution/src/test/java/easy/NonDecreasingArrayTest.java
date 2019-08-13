package easy;

import static org.junit.jupiter.api.Assertions.assertFalse;

import org.junit.jupiter.api.Test;

public class NonDecreasingArrayTest {

    @Test
    void check() {
        NonDecreasingArray function = new NonDecreasingArray();
        assertFalse(function.checkPossibility(new int[]{3, 4, 2, 3}));
    }
}
