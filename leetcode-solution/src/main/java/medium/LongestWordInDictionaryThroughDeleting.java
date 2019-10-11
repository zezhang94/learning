package medium;

import java.util.List;

/**
 * # 524
 * Given a string and a string dictionary, 
 * find the longest string in the dictionary that can be formed by deleting some characters of the given string. 
 * If there are more than one possible results, return the longest word with the smallest lexicographical order. 
 * If there is no possible result, return the empty string.
 * 
 * Example 1:
 *  Input: s = "abpcplea", d = ["ale","apple","monkey","plea"]
 *  Output: "apple"
 * 
 * Example 2:
 *  Input: s = "abpcplea", d = ["a","b","c"]
 *  Output: "a"
 * 
 * Note:
 *  All the strings in the input will only contain lower-case letters.
 *  The size of the dictionary won't exceed 1,000.
 *  The length of all the strings in the input won't exceed 1,000.
 */
public class LongestWordInDictionaryThroughDeleting {

    // TODO: find fatser solution.
    public String findLongestWord(String s, List<String> d) {
        String result = "";
        for (String word : d) {
            if (this.checkIfCanDeleteTo(s, word) > result.length() || 
                this.checkIfCanDeleteTo(s, word) == result.length() && this.compare(result, word) > 0) {
                result = word;
            }
        }
        return result;
    }

    private int checkIfCanDeleteTo(String source, String word) {
        char target;
        int index = 0;
        if (source.length() < word.length()) {
            return 0;
        }
        int containedLength = 0;
        for (int i = 0; i != word.length(); ++i) {
            target = word.charAt(i);
            for (int j = index; j < source.length(); ++j) {
                if (target == source.charAt(j)) {
                    index = j + 1;
                    ++containedLength;
                    break;
                }
            }
        }
        return containedLength == word.length() ? word.length() : 0;
    }

    public int compare(String s1, String s2) {
        if ("".equals(s1)) {
            return -1;
        }
        int limit = s1.length() <= s2.length() ? s1.length() : s2.length();
        for (int index = 0; index != limit; ++index) {
            if (s1.charAt(index) > s2.charAt(index)) {
                return 1;
            } else if (s1.charAt(index) < s2.charAt(index)) {
                return -1;
            }
        }
        // Different length.
        if (s1.length() > s2.length()) {
            return 1;
        }
        if (s1.length() < s2.length()) {
            return -1;
        }
        return 0;
    }
}