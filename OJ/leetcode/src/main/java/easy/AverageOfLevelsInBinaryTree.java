package easy;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * # 637
 * Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
 * Example 1:
 *  Input:
 *      3
 *     / \
 *    9  20
 *      /  \
 *     15   7
 *  Output: [3, 14.5, 11]
 * 
 * Explanation:
 * The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
 * 
 * Note:
 * The range of node's value is in the range of 32-bit signed integer.
 */
public class AverageOfLevelsInBinaryTree {

    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> result = new LinkedList<>();
        Queue<TreeNode> layer = new LinkedList<>();
        layer.offer(root);

        double layerSum = 0;
        int size;
        int i;
        TreeNode temp;
        while (!layer.isEmpty()) {
            size = layer.size();
            i = size;
            while (i > 0) {
                temp = layer.poll();
                layerSum += temp.val;
                if (null != temp.left) {
                    layer.offer(temp.left);
                }
                if (null != temp.right) {
                    layer.offer(temp.right);
                }
                --i;                   
            }
            result.add(layerSum / size);
            layerSum = 0;
        }
        return result;
    }
    
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}