import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class PartitionToKEqualSumSubsets_698 {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = Arrays.stream(nums).sum();
        int mod = sum % k;
        if (mod != 0) {
            return false;
        }
        int quotient = sum / k;
        List<Integer> list = Arrays.stream(nums)
                .boxed().sorted().collect(Collectors.toList());
        if (list.get(list.size() - 1) > quotient) {
            return false;
        }
        while (list.size() > 0 && list.get(list.size() - 1) == quotient) {
            list.remove(list.size() - 1);
            k--;
        }
        List<Integer> groups = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            groups.add(0);
        }
        return search(list, groups, quotient);
    }

    private boolean search(List<Integer> list, List<Integer> groups, int quotient) {
        if (list.size() == 0) {
            return true;
        }
        int candidate = list.remove(list.size() - 1);
        for (int i = 0; i < groups.size(); ++i) {
            int source = groups.get(i);
            if (candidate + source <= quotient) {
                groups.set(i, source + candidate);
                if (search(list, groups, quotient)) {
                    return true;
                }
                groups.set(i, source);
            }
            if (groups.get(i) == 0) {
                break;
            }
        }
        list.add(candidate);
        return false;
    }
}
