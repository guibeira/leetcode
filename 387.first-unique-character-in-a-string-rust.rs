// @leet start
use std::collections::HashMap;
impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let mut words_count = HashMap::new();
        for c in s.chars() {
            let count = words_count.entry(c).or_insert(0);
            *count += 1;
        }
        for (i, c) in s.chars().enumerate() {
            if words_count.get(&c).unwrap_or(&0) == &1 {
                return i as i32;
            }
        }
        -1
    }
}
// @leet end

