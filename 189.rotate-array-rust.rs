// @leet start
impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        for i in (0..k) {
            let last = nums.pop().unwrap();
            nums.insert(0, last);
        }
    }
}
// @leet end

