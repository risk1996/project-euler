pub fn solve(lim: usize) -> usize {
  (0..lim).filter(|i| i % 3 == 0 || i % 5 == 0).sum()
}

#[cfg(test)]
pub mod tests {
  use super::*;

  #[test]
  fn test_solve() {
    let cases = [(10, 23), (1_000, 233_168)];

    for (input, expected) in cases {
      assert_eq!(solve(input), expected);
    }
  }
}
