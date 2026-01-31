use crate::common::sum::FastSum;

pub fn solve(n: usize) -> usize {
  let sum_of_sq = (1..=n).map(|i| i * i).sum::<usize>();
  let sq_of_sum = (1..=n).fast_sum().pow(2);
  sq_of_sum - sum_of_sq
}

#[cfg(test)]
mod tests {
  use super::*;

  #[test]
  fn test_solve() {
    let cases = [(10, 2640), (100, 25164150)];

    for (input, expected) in cases {
      let actual = solve(input);
      assert_eq!(actual, expected);
    }
  }
}
