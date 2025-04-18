pub fn solve(lim: usize) -> usize {
  (0..)
    .try_fold((0, 1, 2), |(even_total, a, b), _| {
      match (a > lim, a % 2 == 0) {
        | (true, _) => Err(even_total),
        | (_, true) => Ok((even_total + a, b, b + a)),
        | _ => Ok((even_total, b, b + a)),
      }
    })
    .unwrap_err()
}

#[cfg(test)]
pub mod tests {
  use super::*;

  #[test]
  fn test_solve() {
    let cases = vec![(89, 2 + 8 + 34), (4_000_000, 4_613_732)];

    for (input, expected) in cases {
      assert_eq!(solve(input), expected);
    }
  }
}
