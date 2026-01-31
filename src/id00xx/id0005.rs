use std::ops::RangeInclusive;

use crate::common::division::Lcm;

pub fn solve(range: &RangeInclusive<usize>) -> usize {
  range.clone().fold(1, Lcm::lcm)
}

#[cfg(test)]
pub mod tests {
  use super::*;

  #[test]
  fn test_solve() {
    let cases = [(1..=10, 2_520), (1..=20, 232_792_560)];

    for (input, expected) in cases {
      assert_eq!(solve(&input), expected);
    }
  }
}
