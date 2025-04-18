use std::collections::HashSet;

use crate::common::sqrt_floor::SqrtFloor;

#[derive(Debug, PartialEq, Eq, Clone)]
pub struct PrimeSieve {
  primes: HashSet<usize>,
}

impl PrimeSieve {
  pub fn of_size(limit: usize) -> Self {
    if limit <= 1 {
      return Self {
        primes: HashSet::new(),
      };
    }

    let mut sieve = vec![true; limit + 1];
    (sieve[0], sieve[1]) = (false, false);

    for i in 2..=limit.sqrt_floor() {
      for j in ((i * i)..=limit).step_by(i) {
        sieve[j] = false;
      }
    }

    Self {
      primes: sieve
        .into_iter()
        .enumerate()
        .filter(|(_, v)| *v)
        .map(|(i, _)| i)
        .collect(),
    }
  }

  pub fn primes(self) -> Vec<usize> {
    let mut primes = Vec::from_iter(self.primes);
    primes.sort();
    primes
  }

  pub fn is_prime(&self, n: usize) -> bool {
    self.primes.contains(&n)
  }
}

#[cfg(test)]
mod tests {
  use super::*;

  #[test]
  fn test_prime_sieve() {
    let cases = vec![
      (1, vec![]),
      (11, vec![2, 3, 5, 7, 11]),
      (300, vec![
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
        97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
        191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
        283, 293,
      ]),
    ];

    for (input, primes) in cases {
      let primes = HashSet::from_iter(primes);
      let expected = PrimeSieve { primes };
      assert_eq!(PrimeSieve::of_size(input), expected);
    }
  }
}
