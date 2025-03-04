def find_prime_factors(number):
  factors_list = []
  divisor_count = 2
  while divisor_count <= number:
    if number % divisor_count == 0:
      factors_list.append(divisor_count)
      number = number // divisor_count
    else:
      divisor_count += 1
  return factors_list

def main():
  print("Prime factors of 630: ",find_prime_factors(630))

main()
