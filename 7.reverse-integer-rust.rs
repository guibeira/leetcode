// @leet start
impl Solution {
    pub fn reverse(x: i32) -> i32 {
        let to_string = x.to_string();
        let reversed = to_string.chars().rev().collect::<String>();

        //println!("f {:?}", reversed);
        let last = reversed.chars().last().unwrap_or(' ');
        //println!("last {:?}", last);

        if '-' == last {
            let mut reversed = reversed.chars().collect::<Vec<char>>();
            reversed.pop();
            reversed.insert(0, '-');

            let reversed = reversed.iter().collect::<String>();
            //println!("negative {:?}", reversed);
            let converted = reversed.parse::<i32>().unwrap_or(0);
            return converted;
        } else {
            reversed.parse::<i32>().unwrap_or(0);
            //println!("positive {:?}", reversed);
            let converted = reversed.parse::<i32>().unwrap_or(0);
            return converted;
        }
        0
    }
}
// @leet end

