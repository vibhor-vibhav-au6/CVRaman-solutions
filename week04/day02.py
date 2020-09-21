# Q1. Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def caps(a):
  l = 0
  u = 0
  for i in a:
    if i != ' ':
      if i.isupper():
        u += 1
      else:
        l += 1
  return(l, u)

print(caps(a))

# Q3. Write a program which counts the no of vowels in a string.

def vowel(a):
  c = 0
  for i in a:
    if i in 'AEIOUaeiou':
      c += 1
  
  return(c)

print(vowel(a))


# Q2. Write a Python function that takes a number as a parameter and check the
# number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that
# has no positive divisors other than 1 and itself.

# naive method
def prime(n):
  if n <=1:
    return False

  for i in range(2,n):
    if n%i == 0:
      return False
  
  return True

# optimised method. checking only till square root of N
import math

def prime2(n):
  if n <=1:
    return False
  if n == 2:
    return True

  d = int(math.sqrt(n))

  for i in range(3, d+1):
    if n%i == 0:
      return False
  
  return True

# further optimization: rejecting even numbers
def prime3(n):
  if n <=1:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False

  d = int(math.sqrt(n))

  for i in range(3, d+1, 2):
    if n%i == 0:
      return False
  
  return True


# code to calculate time of the prime function
import time
t0 = time.time()
for i in range(1000000):
  prime2(i)

t1 = time.time()
print('time taken is'+ str(t1-t0))
