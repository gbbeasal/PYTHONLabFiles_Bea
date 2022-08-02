# Additional basic string exercises
#===========================================================================================
# MA.BEATRIZ SALAZAR - 10015286
#===========================================================================================


# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  if len(s) >= 3:
      if "ing" in s:
          verb = s+'ly'
      else:
          verb = s+'ing'
  else:
    verb = s
  return verb
  return


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  not_i = s.find('not')
  bad_i = s.find('bad')

  if not_i < bad_i:
    s = s.replace(s[not_i:(bad_i+3)], 'good')
  return s
  return


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  #FOR STRING a:
  if (len(a)%2 == 0): #the string length is EVEN
      u_lim = int(len(a)/2)
      af = a[0:u_lim]
      ab = a[(u_lim):len(a)+1]
  else: #string length is ODD
      u_lim2 = int((len(a)/2)+1)
      af = a[0:u_lim2]
      ab = a[(u_lim2):len(a)+1]

  #FOR STRING b:
  if (len(b)%2 == 0):
      u_lim = int(len(b)/2)
      bf = b[0:u_lim]
      bb = b[(u_lim):len(b)+1]
  else:
      u_lim2 = int((len(b)/2)+1)
      bf = b[0:u_lim2]
      bb = b[(u_lim2):len(b)+1]
  output = af+bf+ab+bb
  return output
  return


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
