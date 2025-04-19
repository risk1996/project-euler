use std::ops::RangeInclusive;

use itertools::iproduct;

use crate::common::palindrome::IsPalindrome;

pub fn solve(range: &RangeInclusive<usize>) -> usize {
  iproduct!(range.clone().rev(), range.clone().rev())
    .map(|(i, j)| i * j)
    .filter(usize::is_palindrome)
    .max()
    .unwrap()
}

#[cfg(test)]
pub mod tests {
  use super::*;

  #[test]
  fn test_solve() {
    let cases = vec![(10..=99, 9_009), (100..=999, 906_609)];

    for (input, expected) in cases {
      assert_eq!(solve(&input), expected);
    }
  }
}
