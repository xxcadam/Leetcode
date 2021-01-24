//
//  main.hpp
//  leetcode
//
//  Created by 夏小川 on 2021/1/23.
//

#ifndef main_hpp
#define main_hpp

#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(): val(0), next(nullptr) {}
    ListNode(int x): val(x), next(nullptr) {}
    ListNode(int x, ListNode *next): val(x), next(next){}
};
#endif /* main_hpp */
