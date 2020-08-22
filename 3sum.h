#pragma once
#include<vector>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        vector<int> temp;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            int l = i + 1, r = nums.size() - 1;
            while (l < r)
            {
                int threesum = nums[l] + nums[r] + nums[i];
                if (threesum > 0)
                    r--;
                else if (threesum < 0)
                    l++;
                else {
                    temp = { nums[i], nums[l], nums[r] };
                    if (find(result.begin(), result.end(), temp) == result.end())
                        result.push_back(temp);
                    while (nums[l] == temp[1] && l<r)
                        l++;
                    while (nums[r] == temp[2] && l<r)
                        r--;
                }
            }
        }
        return result;
    }
};