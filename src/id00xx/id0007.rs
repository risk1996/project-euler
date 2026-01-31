use crate::common::prime::PrimeSieve;

pub fn solve(nth: usize) -> usize {
  let zero_indexed_nth = nth.saturating_sub(1);
  let sieve = PrimeSieve::to_nth(zero_indexed_nth);
  sieve.primes()[zero_indexed_nth]
}

#[cfg(test)]
mod tests {
  use super::*;

  #[test]
  fn test_solve() {
    let cases = [(6, 13), (10_001, 104_743)];

    for (input, expected) in cases {
      let actual = solve(input);
      assert_eq!(actual, expected);
    }
  }
}
