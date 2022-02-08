import java.util.*;

public class DifferentWaysToAddParentheses_241 {
    public List<Integer> diffWaysToCompute(String input) {
        Map<String, List<Integer>> record = new HashMap<>();
        return divide(input, record);
    }

    private final static Set<Character> opSet = new HashSet<>(Arrays.asList('+', '-', '*'));

    private List<Integer> divide(String input, Map<String, List<Integer>> record) {
        if (record.containsKey(input)) {
            return record.get(input);
        }
        List<Integer> valueList = new ArrayList<>(32);
        List<Integer> leftList, rightList;
        for (int i = 0; i < input.length(); ++i) {
            if (opSet.contains(input.charAt(i))) {
                leftList = divide(input.substring(0, i), record);
                rightList = divide(input.substring(i + 1), record);
                for (int l : leftList) {
                    for (int r : rightList) {
                        valueList.add(calculate(input.charAt(i), l, r));
                    }
                }
            }
        }
        if (valueList.isEmpty()) {
            valueList.add(Integer.parseInt(input));
        }
        record.put(input, valueList);
        return valueList;
    }

    private int calculate(char op, int v1, int v2) {
        switch (op) {
            case '+':
                return v1 + v2;
            case '-':
                return v1 - v2;
            default:
                return v1 * v2;
        }
    }
}
