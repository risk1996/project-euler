use std::ops::Mul;

use crate::common::sqrt::SqrtFloor;

pub trait IsSquare {
  fn is_square(self) -> bool;
}

impl<T: Copy + Eq + Mul<Output = T> + SqrtFloor> IsSquare for T {
  fn is_square(self) -> bool {
    let sqrt = self.sqrt_floor();
    self == sqrt * sqrt
  }
}

#[cfg(test)]
mod tests {
  use super::*;

  #[test]
  fn test_is_square() {
    let cases = [
      (0u32, true),
      (1, true),
      (2, false),
      (3, false),
      (4, true),
      (5, false),
      (6, false),
      (7, false),
      (8, false),
      (9, true),
      (10, false),
      (100, true),
    ];

    for (input, expected) in cases {
      assert_eq!(input.is_square(), expected);
    }
  }
}
