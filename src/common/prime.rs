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

  pub fn to_nth(zero_indexed_nth: usize) -> Self {
    let nth = (zero_indexed_nth + 1) as f64;
    // NOTE: Using reasonable nth prime upper bound, which holds when n >= 6;
    let upper = (nth * (nth.ln() + nth.ln().ln()) + 1.) as usize;
    let upper = upper.max(5);
    Self::of_size(upper)
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
  fn test_prime_sieve_primes() {
    let cases = [
      (1, vec![]),
      (11, vec![2, 3, 5, 7, 11]),
      (300, vec![
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
        97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
        191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
        283, 293,
      ]),
    ];

    for (size, expected) in cases {
      let sieve = PrimeSieve::of_size(size);
      let actual = sieve.primes();
      assert_eq!(actual, expected);
    }
  }

  #[test]
  fn test_prime_sieve_nth() {
    let cases = [
      (0, 2),
      (1, 3),
      (2, 5),
      (3, 7),
      (4, 11),
      (5, 13),
      (6, 17),
      (99, 541),
      (999, 7_919),
      (9_999, 104_729),
    ];

    for (input, expected) in cases {
      let sieve = PrimeSieve::to_nth(input);
      let primes = sieve.primes();
      assert!(primes.len() >= input);
      assert_eq!(primes[input], expected);
    }
  }
}
