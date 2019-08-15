package easy;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/**
 * AddStringsTest
 */
public class AddStringsTest {

    @Test
    void check() {
        AddStrings function = new AddStrings();
        assertEquals("9133".getBytes(), function.addStrings("9133", "0").getBytes());
    }
}