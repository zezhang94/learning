package medium;

import java.util.List;

/**
 * # 539 Given a list of 24-hour clock time points in "Hour:Minutes" format,
 * find the minimum minutes difference between any two time points in the list.
 * 
 * Example 1: Input: ["23:59","00:00"] Output: 1
 * 
 * Note: The number of time points in the given list is at least 2 and won't
 * exceed 20000. The input time is legal and ranges from 00:00 to 23:59.
 */
public class MinimumTimeDifference {

    public int findMinDifference(List<String> timePoints) {
        int[] timeMinutes = new int[timePoints.size()];
        for (int i = 0; i < timePoints.size(); i++) {
            timeMinutes[i] = timePointToInt(timePoints.get(i));
        } 
        quicksort(timeMinutes, 0, timePoints.size() - 1);

        int min = 24 * 60;
        int difference;
        for (int i = 1; i < timeMinutes.length; i++) {
            difference = timeMinutes[i] - timeMinutes[i - 1];
            if (difference < min) {
                min = difference;
            }
        }
        difference = timeMinutes[0] + 24 * 60 - timeMinutes[timeMinutes.length - 1];
        return min < difference ? min : difference;
    }

    private int timePointToInt(String op) {
        int i = (op.charAt(3) - '0') * 10;
        i += op.charAt(4) - '0';
        i += (op.charAt(1) - '0') * 60;
        i += (op.charAt(0) - '0') * 10 * 60;
        return i;
    }

    private void quicksort(int[] timeMinutes, int left, int right) {
        int pivotIndex;
        if (left < right) {
            pivotIndex = division(timeMinutes, left, right);
            quicksort(timeMinutes, left, pivotIndex - 1);
            quicksort(timeMinutes, pivotIndex + 1, right);
        }
    }

    private int division(int[] timeMinutes, int left, int right) {

        int pivot = timeMinutes[left];
        int i = left + 1;

        for (int j = left + 1; j <= right; ++j) {
            if (timeMinutes[j] < pivot) {
                swap(timeMinutes, i++, j);
            }
        }

        swap(timeMinutes, left, i - 1);
        return i - 1;
    }

    private void swap(int[] timeMinutes, int a, int b) {
        int temp = timeMinutes[a];
        timeMinutes[a] = timeMinutes[b];
        timeMinutes[b] = temp;
    }
}