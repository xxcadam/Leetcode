// You are given two non-empty linked lists representing two non-negative integers. 
// The digits are stored in reverse order and each of their nodes contain a single digit. 
// Add the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Example:

// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8
// Explanation: 342 + 465 = 807.

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sum;
        ListNode *head = new ListNode();
        ListNode *res = head;
        int carry = 0;
        while(l1!=nullptr || l2!=nullptr || carry){
            sum = (l1?l1->val:0) + (l2?l2->val:0) + carry;
            carry = sum/10;
            head->next = new ListNode(sum%10);
            head = head->next;
            l1 = l1? l1->next : l1;
            l2 = l2? l2->next : l2;
        }
        return res->next;
    }
};
