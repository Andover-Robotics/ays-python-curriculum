import ast, requests, os, random

print("<html>")
print("<style>error{color:red;font-weight:bold}success{color:darkgreen;font-weight:bold}hint{color:blue}*[stacktrace]{font-size:9px;color:darkgray;line-height:11px}inline-code{font-family:monospace}</style>")

def report_score(score, maxp):
  score = max(0, score)
  url = "{0}&points={1}".format(os.environ['CODIO_PARTIAL_POINTS_URL'], score)
  requests.get(url)
  print("\n<b>Score:</b> %d out of %d" % (score, maxp))
  
with open('lists/Q3_Insertion.py') as subfile:
  subtext = subfile.read()
  sub = ast.parse(subtext)
  
max_score = 10

def find_type(ast_type, body):
  for elem in body:
    if isinstance(elem, ast_type):
      return elem
  return None

def run():
  classdef = find_type(ast.FunctionDef, sub.body)
  if classdef is None:
    print("<error>There is no function definition in your code!</error>")
    return 0
  if classdef.name != "insert_sorted":
    print("<error>Your function is named '{}', not 'insert_sorted'!</error>".format(classdef.name))
    return 1
  for child in ast.walk(sub):
    if isinstance(child, ast.Call):
      if hasattr(child.func, 'attr') and child.func.attr == 'sort':
        print("<error>You were not supposed to use the list.sort method! Additionally, you should not implement a sorting algorithm.</error>")
        return 1
  return 10

score = run()
try:
  exec(subtext)

  def gen_case(n):
    for i in range(n):
      array = random.sample(range(-200, 200), 20)
      array.sort()
      elem = random.choice(list(set(range(-200, 200)) - set(array)))
      pos = 0
      while pos < len(array) and array[pos] < elem: pos += 1
      yield (array, elem, pos)
    
  for (arr, elem, pos) in gen_case(8):
    array = arr.copy()
    insert_sorted(array, elem)
    
    if array[pos] != elem:
      print("<error>[FAIL] invalid result after insertion of {} into {}</error>".format(elem, arr))
      score -= 1
    else:
      print("<success>[PASS]</success>")
    print("<hr>")
except Exception as e:
  print("<error>Your code raised an exception: {}</error>".format(e))
  score = 2

report_score(score, max_score)

print("</html>")