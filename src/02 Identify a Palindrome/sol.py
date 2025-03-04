import re
def is_palindrome(name):
  name = re.sub(r'[^A-Za-z]',"",name).lower()
  return name == name[::-1]

print(is_palindrome("Go hang a salami, I’m a lasagna hog."))
print(is_palindrome('hello world'))