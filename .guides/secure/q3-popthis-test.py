import ast, requests, os, random, copy

print("<html>")
print("<style>error{color:red;font-weight:bold}success{color:darkgreen;font-weight:bold}hint{color:blue}*[stacktrace]{font-size:9px;color:darkgray;line-height:11px}inline-code{font-family:monospace}</style>")

def report_score(score, maxp):
  score = max(0, score)
  url = "{0}&points={1}".format(os.environ['CODIO_PARTIAL_POINTS_URL'], score)
  requests.get(url)
  print("\n<b>Score:</b> %d out of %d" % (score, maxp))

def random_names():
  return random.sample(["James", "Anna", "Bob", "Alice", "Lucas", "Ethan", "Lily", "David", "John", "Emily", "Sophia"], 6)

score = 6

names = random_names()
original_names = copy.copy(names)

print("<inline-code>names = {}</inline-code>".format(names))

output = []
sys_print = print
print = output.append

with open('Q3_PopThis.py') as subfile:
  subtext = subfile.read()
  sub = ast.parse(subtext)
  exec(subtext)
  
print = sys_print
expected_output = original_names[::2]
expected_names = original_names[1::2]

if len(output) != 3:
  print("<error>Your code printed {} element(s), but it was supposed to print 3!</error>".format(len(output)))

def list_sub(a, b):
  return [x for x in a if x not in b]

if expected_output != output:
  print("<error>Your output did not match the expected output!", end='')
  amb, bma = list_sub(output, expected_output), list_sub(expected_output, output)
  if len(amb) > 0:
    print(" Your output has extraneous elements: <inline-code>{}</inline-code>".format(amb))
  if len(bma) > 0:
    print(" Your output is missing expected elements: <inline-code>{}</inline-code>".format(bma))
  if len(bma) == 0 and len(amb) == 0:
    print(" The order was incorrect. Expected order: <inline-code>{}</inline-code>; Actual order: <inline-code>{}</inline-code>".format(expected_output, output))
    score -= 1
  score -= len(amb) + len(bma)
  print("</error>")
  
if expected_names != names:
  print("<error>The contents of <inline-code>names</inline-code> did not match the expected value!", end='')
  amb, bma = list_sub(names, expected_names), list_sub(expected_names, names)
  if len(amb) > 0:
    print(" The content of <inline-code>names</inline-code> has extraneous elements: <inline-code>{}</inline-code>".format(amb))
  if len(bma) > 0:
    print(" <inline-code>names</inline-code> is missing expected elements: <inline-code>{}</inline-code>".format(bma))
  if len(bma) == 0 and len(amb) == 0:
    print(" The order was incorrect. Expected order: <inline-code>{}</inline-code>; Actual order: <inline-code>{}</inline-code>".format(expected_names, names))
    score -= 1
  score -= len(amb) + len(bma)
  print("</error>")

if score == 6:
  print("<success>Good job</success>")
report_score(score, 6)

print("</html>")