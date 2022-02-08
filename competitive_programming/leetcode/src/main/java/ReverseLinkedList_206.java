public class ReverseLinkedList_206 {
    private class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode reverseList(ListNode head) {
        ListNode cur = null;
        ListNode pre = null;
        while (head != null) {
             cur = head;
             head = head.next;
             cur.next = pre;
             pre = cur;
        }
        return cur;
    }

    public ListNode recursive(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode ans = recursive(head.next);
        // reverse
        head.next.next = head;
        head.next = null;
        // ans is tail node
        return ans;
    }
}
