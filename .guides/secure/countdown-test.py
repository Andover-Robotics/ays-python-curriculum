import os, sys, requests, random
import re
with open('Q5_Countdown.py') as response:
  answer = response.read()

if 'while' not in answer:
  print("You did not implement a `while` loop!")
  sys.exit(1)
if 'for' in answer:
  print("You implemented a `for` loop!")
  sys.exit(1)
  
import io
from contextlib import redirect_stdout

def expected(times):
  return "\n".join(map(str, range(times, 0, -1))) + "\n"

def match(output, expected, norecur=False):
  if output == expected:
    print("Your output matches the expected output exactly")
    return 2
  
  if len(output) > 2 and output.strip() in expected or expected.strip() in output:
    print("Your output partially matched the expected output")
    return 1
  
  if not norecur and match(output[::-1].strip(), expected.strip(), norecur=True) > 0:
    print("You may not have printed the numbers in decreasing order")
    return 1
  
  return 0

def test_times(times):
  try:
    output = None
    with io.StringIO() as buf, redirect_stdout(buf):
      exec(answer)
      output = buf.getvalue()
    return match(output, expected(times))
  except Exception as e:
    print("Something wasn't right with your code.")
    print(e)
    return False
  
score = 0
  
def report_score():
  url = "{0}&points={1}".format(os.environ['CODIO_PARTIAL_POINTS_URL'], score)
  requests.get(url)
  
for i in range(3):
  times = random.randint(50, 100)
  res = test_times(times)
  if res == 2:
    print("[SUCCESS] with times = " + str(times))
  else:
    print("[FAILURE] with times = " + str(times))
  score += res
  print()

report_score()
print("Points Earned: %d out of 6" % score)
if score == 6:
  sys.exit(0)
else:
  sys.exit(2)