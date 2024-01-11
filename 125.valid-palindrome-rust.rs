// @leet start
impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let mut chars = s.chars().collect::<Vec<char>>();

        chars.retain(|c| c.is_ascii_alphanumeric());

        let lower = chars
            .iter()
            .map(|c| c.to_ascii_lowercase())
            .collect::<Vec<char>>();

        let reversed = lower
            .iter()
            .rev()
            .map(|c| c.to_ascii_lowercase())
            .collect::<Vec<char>>();

        lower == reversed
    }
}
// @leet end

