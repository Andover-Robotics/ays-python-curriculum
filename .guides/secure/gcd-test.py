import os, sys, requests, random
import re, math
with open('Q8_GCD.py') as ans:
  answer = ans.read()

if 'while' not in answer:
  print("You did not implement a `while` loop!")
  sys.exit(1)
if 'for' in answer:
  print("You implemented a `for` loop!")
  sys.exit(1)
if 'def' in answer or 'lambda' in answer:
  print("You defined a function or a lambda, which would allow you to use recursion! Remember, no recursion.")
  sys.exit(1)
if 'import math' in answer or 'from math import' in answer:
  print("You may not use math.gcd!")
  sys.exit(1)

import io
from contextlib import redirect_stdout

def expected(a, b):
  while b:
    a, b = b, a % b
  return a

def match(output, expected, norecur=False):
  return str(output) == str(expected)

def test(a, b):
  try:
    output = None
    with io.StringIO() as buf, redirect_stdout(buf):
      exec(answer)
      output = buf.getvalue().strip()
    return match(output, expected(a, b))
  except Exception as e:
    print("Something wasn't right with your code.")
    print(e)
    if 'integer division or modulo by zero' in str(e):
      print("SUGGESTION: Perhaps you forgot to check whether b == 0?")
    return False
  
score = 0
  
def report_score():
  url = "{0}&points={1}".format(os.environ['CODIO_PARTIAL_POINTS_URL'], int(score))
  requests.get(url)
  print("Score: %d / 5" % score)
  
for i in range(20):
  a = random.randint(400, 40000)
  b = random.randint(500, 20000)
  res = test(a, b)
  if not res:
    print("[FAILURE] with a = %d, b = %d" % (a, b))
  else:
    score += 5 / 20.0
    print("[SUCCESS] with a = %d, b = %d" % (a, b))
  print()

report_score()
sys.exit(0 if score == 5 else 1)