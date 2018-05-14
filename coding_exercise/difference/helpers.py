def calculateDifference(number):
  sum_of_squares = 0
  sum_of_numbers = 0
  for x in range(1, number + 1):
    sum_of_squares = sum_of_squares + (x**2)
    sum_of_numbers = sum_of_numbers + x
  print(sum_of_squares)
  print(sum_of_numbers**2)
  return (sum_of_numbers**2) - sum_of_squares