
def main():
  book_path = "books/frankenstein.txt"
  
  print_begin_report(book_path)

  text = get_book_text(book_path)
  num_words = get_num_words(text)
  print(f"{num_words} words found in the document\n")

  num_chars_dict = get_num_characters(text)
  alpha_only_dict = {k:v for k,v in num_chars_dict.items() if k.isalpha()}
  sorted_dict = dict(sorted(alpha_only_dict.items(), key=lambda item: item[1], reverse=True))
  for char in sorted_dict:
    print(f"The '{char}' character was found {num_chars_dict[char]} times")
  
  print_end_report()

def get_book_text(path):
  with open("./books/frankenstein.txt") as f:
    return f.read()

def get_num_words(text):
  words = text.split()
  return len(words)

def get_num_characters(text):
  num_characters = {}
  for c in text.lower():
    if c not in num_characters:
      num_characters[c] = 0
    num_characters[c] += 1
  return dict(sorted(num_characters.items()))

def print_begin_report(path):
  print(f"--- Begin report of {path} ---")

def print_end_report():
  print(f"--- End report ---")
    
main()