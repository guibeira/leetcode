// @leet start
//
use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut numbers = HashMap::new();

        for (i, num) in nums.iter().enumerate() {
            let complement = target - num;

            if numbers.contains_key(&complement) {
                return vec![numbers[&complement], i as i32];
            }

            numbers.insert(num, i as i32);
        }
        vec![]
    }
}
// @leet end
