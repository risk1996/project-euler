use crate::common::{sqrt::SqrtFloor, square::IsSquare};

pub fn solve() -> usize {
  for a in 0usize..=1_000 {
    for b in 0..=a {
      let sum_of_square = a * a + b * b;
      if sum_of_square.is_square() {
        let c = sum_of_square.sqrt_floor();

        if (a + b + c) == 1_000 {
          return a * b * c;
        }
      }
    }
  }

  0
}

#[cfg(test)]
pub mod tests {
  use super::*;

  #[test]
  fn test_solve() {
    let expected = 31_875_000;
    assert_eq!(solve(), expected);
  }
}
