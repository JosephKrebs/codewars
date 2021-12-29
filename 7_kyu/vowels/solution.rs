fn get_count(string: &str) -> usize {
  let mut vowels_count: usize = 0;

  for k in string.chars() {
    if k == 'a' || k == 'e' || k == 'i' || k == 'o' || k == 'u' {
            vowels_count += 1;
            }
      }
    vowels_count
}