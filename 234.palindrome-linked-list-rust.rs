// @leet start
// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn is_palindrome(head: Option<Box<ListNode>>) -> bool {
        if head.is_none() {
            return true;
        }

        let mut lenght = 0;
        let mut ele = Vec::new();
        let mut nxt = head;

        while nxt.is_some() {
            let curr = nxt.unwrap();
            ele.push(curr.val);
            nxt = curr.next;
            lenght += 1;
        }
        let middle = lenght / 2;
        let first_part = &ele[0..middle];

        let mut second_part = Vec::new();
        for i in (middle)..lenght {
            second_part.push(ele[i]);
        }
        second_part.reverse();

        for (i, val) in first_part.iter().enumerate() {
            if *val != second_part[i] {
                return false;
            }
        }

        true
    }
}
// @leet end
