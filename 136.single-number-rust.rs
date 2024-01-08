// @leet start
use std::collections::HashMap;
impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut number_count = HashMap::new();

        for num in nums {
            number_count.entry(num).and_modify(|e| *e += 1).or_insert(1);
        }

        for (num, count) in number_count {
            if count == 1 {
                return num;
            }
        }

        1
    }
}
// @leet end

