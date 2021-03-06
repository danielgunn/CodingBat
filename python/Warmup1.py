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

def parrot_trouble(talking, hour):
  return talking and (hour < 7 or hour > 20)

def makes10(a, b):
  return (a==10 or b==10 or (a+b)==10)

def near_hundred(n):
  return abs(100-n) <= 10 or abs(200-n)<=10

def pos_neg(a, b, negative):
  if (negative):
    return (a < 0 and b < 0)
  return (a > 0 and b < 0) or (a < 0 and b > 0)

def not_string(str):
  if (str.startswith("not")):
    return str
  return "not "+str

def missing_char(str, n):
  return str[:n] + str[n+1:]

def front_back(str):
  if (len(str) == 1):
    return str
  return str[-1:] + str[1:-1] + str[0:1]

def front3(str):
  return 3*str[0:3]

# The following code was generated by the expected_to_assert program
assert sleep_in(False, False) == True
assert sleep_in(True, False) == False
assert sleep_in(False, True) == True
assert sleep_in(True, True) == True
assert monkey_trouble(True, True) == True
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
assert parrot_trouble(True, 6) == True
assert parrot_trouble(True, 7) == False
assert parrot_trouble(False, 6) == False
assert parrot_trouble(True, 21) == True
assert parrot_trouble(False, 21) == False
assert parrot_trouble(False, 20) == False
assert parrot_trouble(True, 23) == True
assert parrot_trouble(False, 23) == False
assert parrot_trouble(True, 20) == False
assert parrot_trouble(False, 12) == False
assert makes10(9, 10) == True
assert makes10(9, 9) == False
assert makes10(1, 9) == True
assert makes10(10, 1) == True
assert makes10(10, 10) == True
assert makes10(8, 2) == True
assert makes10(8, 3) == False
assert makes10(10, 42) == True
assert makes10(12, -2) == True
assert near_hundred(93) == True
assert near_hundred(90) == True
assert near_hundred(89) == False
assert near_hundred(110) == True
assert near_hundred(111) == False
assert near_hundred(121) == False
assert near_hundred(-101) == False
assert near_hundred(-209) == False
assert near_hundred(190) == True
assert near_hundred(209) == True
assert near_hundred(0) == False
assert near_hundred(5) == False
assert near_hundred(-50) == False
assert near_hundred(191) == True
assert near_hundred(189) == False
assert near_hundred(200) == True
assert near_hundred(210) == True
assert near_hundred(211) == False
assert near_hundred(290) == False
assert pos_neg(1, -1, False) == True
assert pos_neg(-1, 1, False) == True
assert pos_neg(-4, -5, True) == True
assert pos_neg(-4, -5, False) == False
assert pos_neg(-4, 5, False) == True
assert pos_neg(-4, 5, True) == False
assert pos_neg(1, 1, False) == False
assert pos_neg(-1, -1, False) == False
assert pos_neg(1, -1, True) == False
assert pos_neg(-1, 1, True) == False
assert pos_neg(1, 1, True) == False
assert pos_neg(-1, -1, True) == True
assert pos_neg(5, -5, False) == True
assert pos_neg(-6, 6, False) == True
assert pos_neg(-5, -6, False) == False
assert pos_neg(-2, -1, False) == False
assert pos_neg(1, 2, False) == False
assert pos_neg(-5, 6, True) == False
assert pos_neg(-5, -5, True) == True
assert not_string('candy') == 'not candy'
assert not_string('x') == 'not x'
assert not_string('not bad') == 'not bad'
assert not_string('bad') == 'not bad'
assert not_string('not') == 'not'
assert not_string('is not') == 'not is not'
assert not_string('no') == 'not no'
assert missing_char('kitten', 1) == 'ktten'
assert missing_char('kitten', 0) == 'itten'
assert missing_char('kitten', 4) == 'kittn'
assert missing_char('Hi', 0) == 'i'
assert missing_char('Hi', 1) == 'H'
assert missing_char('code', 0) == 'ode'
assert missing_char('code', 1) == 'cde'
assert missing_char('code', 2) == 'coe'
assert missing_char('code', 3) == 'cod'
assert missing_char('chocolate', 8) == 'chocolat'
assert front_back('code') == 'eodc'
assert front_back('a') == 'a'
assert front_back('ab') == 'ba'
assert front_back('abc') == 'cba'
assert front_back('') == ''
assert front_back('Chocolate') == 'ehocolatC'
assert front_back('aavJ') == 'Java'
assert front_back('hello') == 'oellh'
assert front3('Java') == 'JavJavJav'
assert front3('Chocolate') == 'ChoChoCho'
assert front3('abc') == 'abcabcabc'
assert front3('abcXYZ') == 'abcabcabc'
assert front3('ab') == 'ababab'
assert front3('a') == 'aaa'
assert front3('') == ''

print('all tests passed successfully')