use crate::common::{prime::PrimeSieve, sqrt_floor::SqrtFloor};

pub fn solve(n: usize) -> usize {
  PrimeSieve::of_size(n.sqrt_floor())
    .primes()
    .into_iter()
    .filter(|p| n % p == 0)
    .max()
    .unwrap_or(n)
}

#[cfg(test)]
pub mod tests {
  use super::*;

  #[test]
  fn test_solve() {
    let cases = [(13_195, 29), (600_851_475_143, 6_857)];

    for (input, expected) in cases {
      assert_eq!(solve(input), expected);
    }
  }
}
