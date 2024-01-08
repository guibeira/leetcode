// @leet start
use std::collections::HashSet;
impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        // check col
        for c in 0..board.len() {
            let mut col = HashSet::new();
            for r in 0..board.len() {
                let col_val = board[r][c];
                if col_val == '.' {
                    continue;
                }
                if col.contains(&col_val) {
                    return false;
                } else {
                    col.insert(col_val);
                }
            }
        }

        // check row
        for r in board.clone() {
            let mut row = HashSet::new();
            for w in r {
                if w == '.' {
                    continue;
                }
                if row.contains(&w) {
                    return false;
                } else {
                    row.insert(w);
                }
            }
        }

        // check box 3x3
        //let mut box_3x3 = HashSet::new();
        for c in (0..9).step_by(3) {
            let col_start = c;
            let col_end = c + 3;
            for r in (0..9).step_by(3) {
                let row_start = r;
                let row_end = r + 3;
                let mut block = HashSet::new();
                for j in row_start..row_end {
                    for i in col_start..col_end {
                        //println!("{}", board[j][i]);
                        let val = board[j][i];
                        if val == '.' {
                            continue;
                        }
                        if block.contains(&val) {
                            return false;
                        } else {
                            block.insert(val);
                        }
                    }
                }
            }
        }

        true
    }
}
// @leet end

