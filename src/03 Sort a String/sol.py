def sort_words(string):
  words_list = string.split(" ")
  return " ".join(sorted(words_list,key=str.lower))
