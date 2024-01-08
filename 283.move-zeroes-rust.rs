use std::slice::range;

// @leet start
impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        let mut index = 0;
        for i in 0..nums.len() {
            let n = nums[index];
            if n == 0 {
                nums.remove(index);
                nums.push(n);
            } else {
                index = index + 1
            }
        }
    }
}
// @leet end

