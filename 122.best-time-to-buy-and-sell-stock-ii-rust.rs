// @leet start
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut previous_price = prices[0];
        let mut total = 0;
        for i in (1..prices.len()) {
            let current_price = prices[i];
            if previous_price < current_price {
                total += current_price - previous_price;
            }
            previous_price = current_price;
        }
        return total;
    }
}
// @leet end

