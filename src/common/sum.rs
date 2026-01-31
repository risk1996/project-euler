use std::ops::{Range, RangeInclusive};

use num_traits::PrimInt;

pub trait FastSum<T> {
  fn fast_sum(&self) -> T;
}

impl<T: PrimInt> FastSum<T> for RangeInclusive<T> {
  fn fast_sum(&self) -> T {
    let zero = T::zero();
    if self.is_empty() {
      return zero;
    }

    let one = T::one();
    let two = one + one;

    let min = *self.start();
    let max = *self.end();

    let term1 = min.saturating_add(max);
    let term2 = max.saturating_sub(min).saturating_add(one);

    match term1 % two == zero {
      | true => (term1 / two) * term2,
      | false => (term2 / two) * term1,
    }
  }
}

impl<T: PrimInt> FastSum<T> for Range<T> {
  fn fast_sum(&self) -> T {
    (self.start..=self.end.saturating_sub(T::one())).fast_sum()
  }
}

#[cfg(test)]
mod tests {
  use super::*;

  #[test]
  fn test_fast_sum_inclusive_range() {
    let cases = [
      ((0isize..=0), 0isize),
      ((3..=3), 3),
      ((1..=100), 5050),
      ((3..=5), 12),
      ((5..=4), 0),
      ((-10..=0), -55),
    ];

    for (input, expected) in cases {
      let actual = input.fast_sum();
      assert_eq!(actual, expected, "{input:?}");
    }
  }

  #[test]
  fn test_fast_sum_range() {
    let cases = [
      ((0isize..0), 0isize),
      ((3..3), 0),
      ((1..101), 5050),
      ((3..6), 12),
      ((-5..5), -5),
      ((5..4), 0),
      ((-10..0), -55),
    ];

    for (input, expected) in cases {
      let actual = input.fast_sum();
      assert_eq!(actual, expected, "{input:?}");
    }
  }
}
