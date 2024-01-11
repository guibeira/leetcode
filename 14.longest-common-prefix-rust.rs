pub struct Solution;
// @leet start
impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut ans = String::new();
        //println!("strs={:?}", strs);
        let mut v = strs.clone();
        v.sort();
        //println!("v={:?}", v);
        let first = v[0].clone();
        let last = v[v.len() - 1].clone();
        for (i, c) in first.chars().enumerate() {
            if last.chars().nth(i).unwrap_or(' ') != c {
                return ans;
            }
            ans.push(c);
        }
        ans
    }
}
// @leet end
//
fn main() {
    let input = vec![
        "flower".to_string(),
        "flow".to_string(),
        "flight".to_string(),
    ];
    let solution = Solution::longest_common_prefix(input);

    println!("solution={}", solution);
}
