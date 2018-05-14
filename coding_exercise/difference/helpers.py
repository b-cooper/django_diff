def calculateDifference(number):
  sum_of_squares = 0
  sum_of_numbers = 0
  for x in range(1, number + 1):
    sum_of_squares = sum_of_squares + (number**2)
    sum_of_numbers = sum_of_numbers + number
  return sum_of_squares - sum_of_numbers