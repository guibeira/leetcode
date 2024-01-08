// @leet start
impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
        let size = matrix.len();

        let negative_range = (0..size).rev();
        let mut new_matrix = Vec::new();

        for c in negative_range.clone() {
            let mut new_order = Vec::new();
            for r in 0..size {
                //println!("{}", matrix[c][r]);
                let value = matrix[c][r];
                new_order.push(matrix[c][r]);
            }

            new_matrix.push(new_order);
        }

        for (col_index, col) in new_matrix.iter().enumerate() {
            for (r_index, val) in col.iter().enumerate() {
                //println!("c={}, r={}, val={}", col_index, r_index, val);
                matrix[r_index][col_index] = *val
            }
        }
    }
}
// @leet end
