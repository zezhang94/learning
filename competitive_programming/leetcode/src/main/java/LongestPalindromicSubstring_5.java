public class LongestPalindromicSubstring_5 {

    public String longestPalindrome(String s) {
        int start = 0;
        int maxLength = 1;
        for (int i = 0; i < s.length() - 1; ++i) {
            int length = Math.max(longestFromCenter(i, i, s), longestFromCenter(i, i + 1, s));
            if (maxLength < length) {
                maxLength = length;
                start = i -  (maxLength - 1) / 2;
            }
        }
        return s.substring(start, start + maxLength);
    }

    private int longestFromCenter(int left, int right, String s) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            --left;
            ++right;
        }
        return right - left - 1;
    }

}
