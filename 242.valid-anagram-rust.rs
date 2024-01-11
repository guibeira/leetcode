// @leet start
use std::collections::HashMap;
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut s_count = HashMap::new();
        let mut t_count = HashMap::new();

        for c in s.chars() {
            let count = s_count.entry(c).or_insert(0);
            *count += 1;
        }
        for c in t.chars() {
            let count = t_count.entry(c).or_insert(0);
            *count += 1;
        }

        for (k, v) in s_count.iter() {
            if t_count.get(k).unwrap_or(&0) != v {
                return false;
            }
        }

        for (k, v) in t_count.iter() {
            if s_count.get(k).unwrap_or(&0) != v {
                return false;
            }
        }

        true
    }
}
// @leet end

