package easy;

/**
 * 434
 * Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
 * Please note that the string does not contain any non-printable characters.
 * 
 * Example:
 * Input: "Hello, my name is John"
 * Output: 5
 */
public class NumberOfSegmentsInAString {

    public int countSegments(String s) {

        if (null == s || 0 == s.length()) {
            return 0;
        }

        int count = 0;
        if (s.charAt(0) != ' ') {
            ++count;
        }
        for (int i = 0; i != s.length() - 1; i++) {
            if (' ' == s.charAt(i) && s.charAt(i) - s.charAt(i + 1) != 0) {
                ++count;
            }
        }

        return count;
    }
}