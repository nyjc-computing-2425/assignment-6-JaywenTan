from datetime import datetime
import time


# Part 1
def clock(n):
    # Your code here
  """
  returns current time changing every second determined by n
  parameters:
  n - int
  """
  for x in range(n):
    print(datetime.strftime(datetime.now(),"%H:%M:%S"),end = "\r")
    time.sleep(1)
  pass

# Part 2
def lcm(a, b):
    # Your code here
  """
  returns lowest common multipler of a and b
  parameters:
  a - int
  b - int
  """
  if a == b:
    lcm = a
  else:
    c = a
    d = b
    while a != b:
      if a > b:
        b += d
      elif a < b:
        a += c
    lcm = a
  return lcm


# Part 3
def gcf(a, b):
    # Your code here
  """
  returns greatest common factor
  parameters:
  a - int
  b - int
  """
  while b != 0:
    r = a % b
    a = b
    b = r
  gcd = a
  return gcd
    
    
