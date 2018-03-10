def sleep_in(weekday, vacation):
  return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def sum_double(a, b):
  if (a==b):
    return 2 * (a + b)
  return a + b

def diff21(n):
  if (n > 21):
    return (n - 21) * 2
  return (21 - n)


assert sleep_in(False, False) == True	
assert sleep_in(False, True) == True	
assert sleep_in(True, False) == False
assert sleep_in(True, True) == True
assert monkey_trouble(True,True) == True
assert monkey_trouble(False, False) == True
assert monkey_trouble(True, False) == False
assert monkey_trouble(False, True) == False
assert sum_double(1, 2) == 3
assert sum_double(3, 2) == 5
assert sum_double(2, 2) == 8
assert sum_double(-1, 0) == -1
assert sum_double(3, 3) == 12
assert sum_double(0, 0) == 0	
assert sum_double(0, 1) == 1
assert sum_double(3, 4) == 7
assert diff21(19) == 2
assert diff21(10) == 11
assert diff21(21) == 0
assert diff21(22) == 2
assert diff21(25) == 8
assert diff21(30) == 18
assert diff21(0) == 21
assert diff21(1) == 20
assert diff21(2) == 19
assert diff21(-1) == 22
assert diff21(-2) == 23
assert diff21(50) == 58

print("All tests passed successfully")