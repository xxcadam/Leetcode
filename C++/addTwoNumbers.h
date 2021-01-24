//
//  addTwoNumbers.h
//  leetcode
//
//  Created by 夏小川 on 2021/1/24.
//

#ifndef addTwoNumbers_h
#define addTwoNumbers_h
#include "main.hpp"

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *result = new ListNode();
        ListNode* head = result;
        
        int adder = 0;
        while (l1 != nullptr && l2 != nullptr ) {
            int sum = l1->val + l2->val + adder;
            
            head->next = new ListNode(sum%10);
            
            if (sum >= 10)
                adder = 1;
            else
                adder = 0;
            head = head->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        
        if (l1 != nullptr) {
            if (adder == 1)
                head->next = addTwoNumbers(new ListNode(1), l1);
            else
                head->next = addTwoNumbers(new ListNode(), l1);
        } else if(l2 != nullptr ){
            if (adder == 1)
                head->next = addTwoNumbers(new ListNode(1), l2);
            else
                head->next = addTwoNumbers(new ListNode(), l2);
        }
        else if(adder == 1)
            head->next = new ListNode(1);
        return result->next;
    }
};

#endif /* addTwoNumbers_h */
