def string_times(str, n):
  return n*str

def front_times(str, n):
  return str[:3]*n

def string_bits(str):
  t = ""
  for i in range(0,len(str),2):
    t += str[i:i+1]
  return t

def string_splosion(str):
  t = ""
  for i in range(len(str)):
    t += str[:i+1]
  return t

def last2(str):
  t = 0
  s = str[-2:]
  for i in range(0,len(str)-2):
    if str[i:i+2] == s:
      t += 1
  return t

def array_count9(nums):
  t = 0
  for n in nums:
    if n == 9:
      t += 1
  return t

def array_front9(nums):
  for x in nums[:3]:
    if x == 9:
      return True
  return False

def array123(nums):
  w = 0
  for n in nums:
    if n == (w+1):
      w += 1
    if w == 3:
      return True
  return False

def string_match(a, b):
  t = 0
  for i in range(len(a)-1):
    if (a[i:i+2] == b[i:i+2]):
      t += 1
  return t

# the following is generated from expected_input program
assert string_times('Hi', 2) == 'HiHi'
assert string_times('Hi', 3) == 'HiHiHi'
assert string_times('Hi', 1) == 'Hi'
assert string_times('Hi', 0) == ''
assert string_times('Hi', 5) == 'HiHiHiHiHi'
assert string_times('Oh Boy!', 2) == 'Oh Boy!Oh Boy!'
assert string_times('x', 4) == 'xxxx'
assert string_times('', 4) == ''
assert string_times('code', 2) == 'codecode'
assert string_times('code', 3) == 'codecodecode'
assert front_times('Chocolate', 2) == 'ChoCho'
assert front_times('Chocolate', 3) == 'ChoChoCho'
assert front_times('Abc', 3) == 'AbcAbcAbc'
assert front_times('Ab', 4) == 'AbAbAbAb'
assert front_times('A', 4) == 'AAAA'
assert front_times('', 4) == ''
assert front_times('Abc', 0) == ''
assert string_bits('Hello') == 'Hlo'
assert string_bits('Hi') == 'H'
assert string_bits('Heeololeo') == 'Hello'
assert string_bits('HiHiHi') == 'HHH'
assert string_bits('') == ''
assert string_bits('Greetings') == 'Getns'
assert string_bits('Chocoate') == 'Coot'
assert string_bits('pi') == 'p'
assert string_bits('Hello Kitten') == 'HloKte'
assert string_bits('hxaxpxpxy') == 'happy'
assert string_splosion('Code') == 'CCoCodCode'
assert string_splosion('abc') == 'aababc'
assert string_splosion('ab') == 'aab'
assert string_splosion('x') == 'x'
assert string_splosion('fade') == 'ffafadfade'
assert string_splosion('There') == 'TThTheTherThere'
assert string_splosion('Kitten') == 'KKiKitKittKitteKitten'
assert string_splosion('Bye') == 'BByBye'
assert string_splosion('Good') == 'GGoGooGood'
assert string_splosion('Bad') == 'BBaBad'
assert last2('hixxhi') == 1
assert last2('xaxxaxaxx') == 1
assert last2('axxxaaxx') == 2
assert last2('xxaxxaxxaxx') == 3
assert last2('xaxaxaxx') == 0
assert last2('xxxx') == 2
assert last2('13121312') == 1
assert last2('11212') == 1
assert last2('13121311') == 0
assert last2('1717171') == 2
assert last2('hi') == 0
assert last2('h') == 0
assert last2('') == 0
assert array_count9([1, 2, 9]) == 1
assert array_count9([1, 9, 9]) == 2
assert array_count9([1, 9, 9, 3, 9]) == 3
assert array_count9([1, 2, 3]) == 0
assert array_count9([]) == 0
assert array_count9([4, 2, 4, 3, 1]) == 0
assert array_count9([9, 2, 4, 3, 1]) == 1
assert array_front9([1, 2, 9, 3, 4]) == True
assert array_front9([1, 2, 3, 4, 9]) == False
assert array_front9([1, 2, 3, 4, 5]) == False
assert array_front9([9, 2, 3]) == True
assert array_front9([1, 9, 9]) == True
assert array_front9([1, 2, 3]) == False
assert array_front9([1, 9]) == True
assert array_front9([5, 5]) == False
assert array_front9([2]) == False
assert array_front9([9]) == True
assert array_front9([]) == False
assert array_front9([3, 9, 2, 3, 3]) == True
assert array123([1, 1, 2, 3, 1]) == True
assert array123([1, 1, 2, 4, 1]) == False
assert array123([1, 1, 2, 1, 2, 3]) == True
assert array123([1, 1, 2, 1, 2, 1]) == False
assert array123([1, 2, 3, 1, 2, 3]) == True
assert array123([1, 2, 3]) == True
assert array123([1, 1, 1]) == False
assert array123([1, 2]) == False
assert array123([1]) == False
assert array123([]) == False
assert string_match('xxcaazz', 'xxbaaz') == 3
assert string_match('abc', 'abc') == 2
assert string_match('abc', 'axc') == 0
assert string_match('hello', 'he') == 1
assert string_match('he', 'hello') == 1
assert string_match('h', 'hello') == 0
assert string_match('', 'hello') == 0
assert string_match('aabbccdd', 'abbbxxd') == 1
assert string_match('aaxxaaxx', 'iaxxai') == 3
assert string_match('iaxxai', 'aaxxaaxx') == 3

print("All tests passed successfully")
