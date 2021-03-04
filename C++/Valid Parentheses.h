//
//  Valid Parentheses.h
//  leetcode
//
//  Created by 夏小川 on 2021/3/3.
//

#ifndef Valid_Parentheses_h
#define Valid_Parentheses_h
#include"main.hpp"

class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        for(char e:s){
            if (e == '(' || e == '{' || e == '[')
                stack.push_back(e);
            else if (e == ')') {
                if (stack.empty() || stack.back() != '(')
                    return false;
                stack.pop_back();
            }
            else if (e == '}') {
                if (stack.empty() || stack.back() != '{')
                    return false;
                stack.pop_back();
            }
            else if (e == ']') {
                if (stack.empty() || stack.back() != '[')
                    return false;
                stack.pop_back();
            }
        }
        if (stack.empty())
            return true;
        else
            return false;
    }
};


#endif /* Valid_Parentheses_h */
