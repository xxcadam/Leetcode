//
//  ContainerWithMostWater.h
//  leetcode
//
//  Created by 夏小川 on 2021/2/14.
//

#ifndef ContainerWithMostWater_h
#define ContainerWithMostWater_h
#include "main.hpp"
class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0, j = height.size() - 1;
        if (j < 1)
            return 0;
        int max_area = 0;
        int area = 0;
        while (i < j){
            if (height[i] <= height[j]){
                area = height[i] * (j - i);
                i++;
            }
            else {
                area = height[j] * (j - i);
                j--;
            }
            if (area > max_area)
                max_area = area;
        }
        return max_area;
    }
};

#endif /* ContainerWithMostWater_h */
