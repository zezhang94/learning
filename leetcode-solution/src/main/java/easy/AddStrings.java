package easy;

/**
 * # 415
 * Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
 * 
 * Note:
 *  The length of both num1 and num2 is < 5100.
 *  Both num1 and num2 contains only digits 0-9.
 *  Both num1 and num2 does not contain any leading zero.
 *  You must not use any built-in BigInteger library or convert the inputs to integer directly.
 */
public class AddStrings {

    public String addStrings(String num1, String num2) {
        
        StringBuilder result = new StringBuilder();
        int carry = 0;
        int temp = 0;
        int i;
        int j;
    
        for (i = num1.length() - 1, j = num2.length() - 1; i >= 0 && j >= 0; i--, j--) {
            temp = (num1.charAt(i) - '0') + (num2.charAt(j) - '0');
            result.append((temp + carry) % 10);
            carry = (temp + carry) / 10;
        }

        temp = i > j ? i : j;
        num1 = i > j ? num1 : num2;
        j = temp;
        for (i = j; i >= 0; i--) {
            temp = num1.charAt(i) - '0';
            result.append((temp + carry) % 10);
            carry = (temp + carry) / 10;
        }

        if (carry > 0) {
            result.append(1);
        }

        return result.reverse().toString();
    }

}