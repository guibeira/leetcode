// @leet start
use std::collections::HashSet;
impl Solution {
    pub fn intersect(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        if nums1.len() > nums2.len() {
            return Solution::intersect(nums2, nums1);
        } else {
            //println!("nums1: {:?}, nums2: {:?}", nums1, nums2);
            let mut result = Vec::new();
            let mut nums1 = nums1;
            for num in nums2 {
                if nums1.contains(&num) {
                    result.push(num);
                    nums1.remove(nums1.iter().position(|&x| x == num).unwrap());
                }
            }
            return result;
        }
    }
}
// @leet end

