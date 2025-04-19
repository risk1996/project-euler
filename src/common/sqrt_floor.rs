use num_traits::{AsPrimitive, FromPrimitive, PrimInt, Unsigned};

pub trait SqrtFloor {
  fn sqrt_floor(self) -> Self;
}

impl<T: PrimInt + AsPrimitive<f64> + FromPrimitive + Unsigned> SqrtFloor for T {
  fn sqrt_floor(self) -> Self {
    Self::from(self.as_().sqrt()).unwrap()
  }
}

#[cfg(test)]
mod tests {

  use super::*;

  #[test]
  fn test_sqrt_floor() {
    let cases = vec![(0u32, 0), (1, 1), (5, 2), (9, 3), (24, 4)];

    for (input, expected) in cases {
      assert_eq!(input.sqrt_floor(), expected);
    }
  }
}
