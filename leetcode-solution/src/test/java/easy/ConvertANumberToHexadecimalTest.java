package easy;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/**
 * ConvertANumberToHexadecimalTest
 */
public class ConvertANumberToHexadecimalTest {

    @Test
    public void check() {
        ConvertANumberToHexadecimal function = new ConvertANumberToHexadecimal();
        assertEquals("1a", function.toHex(26));
        assertEquals("841", function.toHex(2113));
        assertEquals("270f", function.toHex(9999));
    }
}