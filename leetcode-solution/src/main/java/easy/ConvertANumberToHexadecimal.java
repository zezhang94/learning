package easy;

/**
 * 405
 * Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.
 * 
 * Note:
 *  All letters in hexadecimal (a-f) must be in lowercase.
 *  The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
 *  The given number is guaranteed to fit within the range of a 32-bit signed integer.
 *  You must not use any method provided by the library which converts/formats the number to hex directly.
 * 
 * Example 1:
 *  Input: 26
 *  Output: "1a"
 * 
 * Example 2:
 *  Input: -1
 *  Output: "ffffffff"
 */
public class ConvertANumberToHexadecimal {

    public String toHex(int num) {
        if (0 == num) {
            return "0";
        }

        char[] index = new char[] {
            '0', '1', '2', '3', 
            '4', '5', '6', '7', 
            '8', '9', 'a', 'b', 
            'c', 'd', 'e', 'f'
        };

        int[] _32bits = new int[32];

        // Covert int to 32 bits.
        int temp = num;
        if (temp < 0)  {
            temp = -temp;
        }
        for (int i = 0; i < 32; i++) {
            _32bits[i] = temp % 2;
            temp = temp / 2;
        }

        // If num is negative, negating num the plus 1.
        if (num < 0) {
            int carry = 1;
            for (int i = 0; i < 32; i++) {
                temp = (_32bits[i] + 1) % 2;
                _32bits[i] = (temp + carry) % 2;
                carry = (temp + carry) / 2;
            }
        }

        StringBuilder result = new StringBuilder();
        boolean isHeadZero = true;
        for (int i = 7; i >= 0; i--) {
            temp = 4 * i;
            temp = _32bits[temp] * 1 + _32bits[temp + 1] * 2 + _32bits[temp + 2] * 4 + _32bits[temp + 3] * 8;
            if (isHeadZero) {
                if (temp != 0) {
                    result.append(index[temp]);
                    isHeadZero = false;
                }
                continue;
            }
            result.append(index[temp]);
        }

        return result.toString();
    }

    // TODO: add comment
    public String toHexSimple(int num) {
        if (num == 0) {
            return "0";
        }
        String hexMap = "0123456789abcdef";
        StringBuilder result = new StringBuilder();
        int digit = 0;
        while (num != 0) {
            digit = num & 15;
            result.insert(0, hexMap.charAt(digit));
            num >>>= 4;
        }
        return result.toString();
    }
}