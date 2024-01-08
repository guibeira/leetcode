use std::ops::Add;

// @leet start
impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut digits = digits;
        let mut index: isize = digits.len() as isize - 1;
        while index >= 0 {
            let digit = digits[index as usize];
            if digit != 9 {
                digits[index as usize] = digit + 1;
                return digits;
            } else {
                digits[index as usize] = 0;
            }
            index -= 1;
        }
        if digits[0] == 0 {
            digits.insert(0, 1);
        }
        digits
    }
}
// @leet end
