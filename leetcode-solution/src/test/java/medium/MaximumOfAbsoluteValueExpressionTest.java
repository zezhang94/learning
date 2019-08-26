package medium;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class MaximumOfAbsoluteValueExpressionTest {

    @Test
    public void check() {
        MaximumOfAbsoluteValueExpression f = new MaximumOfAbsoluteValueExpression();
        assertEquals(13, f.stupidWay(new int[] {1, 2, 3, 4}, new int[] {-1, 4, 5, 6}));
        assertEquals(20, f.stupidWay(new int[] {1, -2, -5, 0, 10}, new int[] {0, -2, -1, -7, -4}));
    }  
}