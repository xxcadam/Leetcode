//
//  lengthOfLongestSubString.h
//  leetcode
//
//  Created by 夏小川 on 2021/1/24.
//

#ifndef lengthOfLongestSubString_h
#define lengthOfLongestSubString_h
#include "main.hpp"
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char> charset;
        int res = 0;
        int l = 0;
        
        for(int r = 0, r < s.size(); r++) {
            while (charset.find(s[r]) != charset.end()) {
                charset.erase(s[l]);
                l += 1;
            }
            charset.insert(s[r]);
            res = max(res, r - l + 1);
        }
        return res;
    }
};

#endif /* lengthOfLongestSubString_h */
