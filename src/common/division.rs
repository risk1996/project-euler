use std::ops::{Div, Mul, Rem};

use num_traits::{PrimInt, Unsigned, Zero};

pub trait Gcd {
  fn gcd(self, other: Self) -> Self;
}

impl<T: PrimInt + Rem<T> + Zero + Unsigned> Gcd for T {
  fn gcd(self, other: Self) -> Self {
    let mut a = other % self;
    let mut b = self;

    while a != T::zero() {
      (a, b) = (b % a, a);
    }

    b
  }
}

pub trait Lcm {
  fn lcm(self, other: Self) -> Self;
}

impl<T: PrimInt + Gcd + Mul<T, Output = T> + Div<T, Output = T>> Lcm for T {
  fn lcm(self, other: Self) -> Self {
    self * other / self.gcd(other)
  }
}

#[cfg(test)]
mod tests {
  use super::*;

  #[test]
  fn test_gcd() {
    let cases = [
      ((4usize, 4), 4),
      ((5, 5), 5),
      ((6, 4), 2),
      ((5, 7), 1),
      ((9, 15), 3),
      ((24, 74), 2),
      ((36, 60), 12),
      ((480, 50), 10),
      ((360, 778), 2),
    ];

    for ((a, b), expected) in cases {
      assert_eq!(a.gcd(b), expected);
    }
  }

  #[test]
  fn test_lcm() {
    let cases = [
      ((4usize, 4), 4),
      ((5, 5), 5),
      ((6, 4), 12),
      ((5, 7), 35),
      ((9, 15), 45),
      ((24, 74), 888),
      ((36, 60), 180),
      ((480, 50), 2_400),
      ((360, 778), 140_040),
    ];

    for ((a, b), expected) in cases {
      assert_eq!(a.lcm(b), expected);
    }
  }
}
