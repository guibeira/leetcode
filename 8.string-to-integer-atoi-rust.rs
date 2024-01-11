// @leet start
impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        let mut chars = s.chars().collect::<Vec<char>>();
        chars.retain(|c| !c.is_whitespace());

        let mut result = String::new();
        let mut is_negative = false;
        for (i, c) in chars.iter().enumerate() {
            if i == 0 && *c == '-' {
                is_negative = true;
                continue;
            }
            if i == 0 && *c == '+' {
                continue;
            }
            if c.is_ascii_digit() {
                result.push(*c);
            } else {
                break;
            }
        }

        if result.is_empty() {
            return 0;
        }

        let mut result = result.parse::<i64>().unwrap_or(0);
        if is_negative {
            result = -result;
        }

        if result > i32::MAX as i64 {
            return i32::MAX;
        }
        if result < i32::MIN as i64 {
            return i32::MIN;
        }

        result as i32
    }
}
// @leet end

