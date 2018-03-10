def hello_name(name):
  return "Hello " + name + "!"

def make_abba(a, b):
  return a + b + b + a

def make_tags(tag, word):
  return "<{0}>{1}</{0}>".format(tag,word)

def make_out_word(out, word):
  return out[:2] + word + out[2:]

def extra_end(str):
  return 3*str[-2:]

def first_two(str):
  return str[:2]

def first_half(str):
  return str[:len(str)//2]

def without_end(str):
  return str[1:-1]

def combo_string(a, b):
  s = b
  l = a
  if len(a) < len(b):
    s = a
    l = b
  return s + l + s

def non_start(a, b):
  return a[1:] + b[1:]

def left2(str):
  return str[2:] + str[:2]

# The following code was generated by the expected_to_assert program
assert hello_name('Bob') == 'Hello Bob!'
assert hello_name('Alice') == 'Hello Alice!'
assert hello_name('X') == 'Hello X!'
assert hello_name('Dolly') == 'Hello Dolly!'
assert hello_name('Alpha') == 'Hello Alpha!'
assert hello_name('Omega') == 'Hello Omega!'
assert hello_name('Goodbye') == 'Hello Goodbye!'
assert hello_name('ho ho ho') == 'Hello ho ho ho!'
assert hello_name('xyz!') == 'Hello xyz!!'
assert hello_name('Hello') == 'Hello Hello!'
assert make_abba('Hi', 'Bye') == 'HiByeByeHi'
assert make_abba('Yo', 'Alice') == 'YoAliceAliceYo'
assert make_abba('What', 'Up') == 'WhatUpUpWhat'
assert make_abba('aaa', 'bbb') == 'aaabbbbbbaaa'
assert make_abba('x', 'y') == 'xyyx'
assert make_abba('x', '') == 'xx'
assert make_abba('', 'y') == 'yy'
assert make_abba('Bo', 'Ya') == 'BoYaYaBo'
assert make_abba('Ya', 'Ya') == 'YaYaYaYa'
assert make_tags('i', 'Yay') == '<i>Yay</i>'
assert make_tags('i', 'Hello') == '<i>Hello</i>'
assert make_tags('cite', 'Yay') == '<cite>Yay</cite>'
assert make_tags('address', 'here') == '<address>here</address>'
assert make_tags('body', 'Heart') == '<body>Heart</body>'
assert make_tags('i', 'i') == '<i>i</i>'
assert make_tags('i', '') == '<i></i>'
assert make_out_word('<<>>', 'Yay') == '<<Yay>>'
assert make_out_word('<<>>', 'WooHoo') == '<<WooHoo>>'
assert make_out_word('[[]]', 'word') == '[[word]]'
assert make_out_word('HHoo', 'Hello') == 'HHHellooo'
assert make_out_word('abyz', 'YAY') == 'abYAYyz'
assert extra_end('Hello') == 'lololo'
assert extra_end('ab') == 'ababab'
assert extra_end('Hi') == 'HiHiHi'
assert extra_end('Candy') == 'dydydy'
assert extra_end('Code') == 'dedede'
assert first_two('Hello') == 'He'
assert first_two('abcdefg') == 'ab'
assert first_two('ab') == 'ab'
assert first_two('a') == 'a'
assert first_two('') == ''
assert first_two('Kitten') == 'Ki'
assert first_two('hi') == 'hi'
assert first_two('hiya') == 'hi'
assert first_half('WooHoo') == 'Woo'
assert first_half('HelloThere') == 'Hello'
assert first_half('abcdef') == 'abc'
assert first_half('ab') == 'a'
assert first_half('') == ''
assert first_half('0123456789') == '01234'
assert first_half('kitten') == 'kit'
assert without_end('Hello') == 'ell'
assert without_end('java') == 'av'
assert without_end('coding') == 'odin'
assert without_end('code') == 'od'
assert without_end('ab') == ''
assert without_end('Chocolate!') == 'hocolate'
assert without_end('kitten') == 'itte'
assert without_end('woohoo') == 'ooho'
assert combo_string('Hello', 'hi') == 'hiHellohi'
assert combo_string('hi', 'Hello') == 'hiHellohi'
assert combo_string('aaa', 'b') == 'baaab'
assert combo_string('b', 'aaa') == 'baaab'
assert combo_string('aaa', '') == 'aaa'
assert combo_string('', 'bb') == 'bb'
assert combo_string('aaa', '1234') == 'aaa1234aaa'
assert combo_string('aaa', 'bb') == 'bbaaabb'
assert combo_string('a', 'bb') == 'abba'
assert combo_string('bb', 'a') == 'abba'
assert combo_string('xyz', 'ab') == 'abxyzab'
assert non_start('Hello', 'There') == 'ellohere'
assert non_start('java', 'code') == 'avaode'
assert non_start('shotl', 'java') == 'hotlava'
assert non_start('ab', 'xy') == 'by'
assert non_start('ab', 'x') == 'b'
assert non_start('x', 'ac') == 'c'
assert non_start('a', 'x') == ''
assert non_start('kit', 'kat') == 'itat'
assert non_start('mart', 'dart') == 'artart'
assert left2('Hello') == 'lloHe'
assert left2('java') == 'vaja'
assert left2('Hi') == 'Hi'
assert left2('code') == 'deco'
assert left2('cat') == 'tca'
assert left2('12345') == '34512'
assert left2('Chocolate') == 'ocolateCh'
assert left2('bricks') == 'icksbr'

print('all tests passed successfully')