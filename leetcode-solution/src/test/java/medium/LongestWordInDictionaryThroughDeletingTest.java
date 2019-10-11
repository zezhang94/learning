package medium;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.Arrays;

import org.junit.jupiter.api.Test;

/**
 * LongestWordInDictionaryThroughDeletingTest
 */
public class LongestWordInDictionaryThroughDeletingTest {

    @Test
    public void check() {
        LongestWordInDictionaryThroughDeleting f = new LongestWordInDictionaryThroughDeleting();
        assertEquals("apple", f.findLongestWord("abpcplea", Arrays.asList("ale","apple","monkey","plea")));
        assertEquals("a", f.findLongestWord("abpcplea", Arrays.asList("a","b","c")));
        assertEquals("ab", f.findLongestWord("bab", Arrays.asList("ba","ab","a","b")));
        assertEquals("ewaf", f.findLongestWord("aewfafwafjlwajflwajflwafj", Arrays.asList("apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf")));
        assertEquals("best", f.findLongestWord("wordgoodgoodgoodbestword", Arrays.asList("word","good","best","good")));
    }
}