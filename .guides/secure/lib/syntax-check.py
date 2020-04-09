import ast, traceback, sys

# Accepts a filename relative to ~/workspace
filename = sys.argv[1]

try:
  with open(filename) as subfile:
    sub = ast.parse(subfile.read(), filename=filename)
except Exception as e:
  print('Syntax error found!')
  for line in traceback.format_exception_only(SyntaxError, e):
    print(line, end='')
  exit(1)