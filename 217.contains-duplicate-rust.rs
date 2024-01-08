// @leet start
use std::collections::HashSet;
impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut numbers = HashSet::new();
        for num in nums {
            if numbers.contains(&num) {
                return true;
            }
            numbers.insert(num);
        }
        return false;
    }
}
// @leet end

