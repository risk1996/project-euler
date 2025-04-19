pub trait IsPalindrome {
  fn is_palindrome(&self) -> bool;
}

impl<T: ToString> IsPalindrome for T {
  fn is_palindrome(&self) -> bool {
    let str_value = self.to_string();
    let reverse = str_value.chars().rev().collect::<String>();

    str_value == reverse
  }
}
