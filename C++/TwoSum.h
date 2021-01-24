//
//  TwoSum.h
//  leetcode
//
//  Created by 夏小川 on 2021/1/23.
//

#ifndef TwoSum_h
#define TwoSum_h

#include "main.hpp"

class Solution {
public:
    void sample() {
        cout<<"hello world2"<<endl;
    }
    
    vector<int> twoSum (vector<int> nums, int target){
        unordered_map<int, int> dic;
        for (int i=0; i< nums.size(); i++) {
            int diff = target - nums[i];
            if (dic.count(diff))
                return { dic[diff], i };
            dic[nums[i]] = i;
        }
        return {};
    }
};
#endif /* TwoSum_h */
