import ast

with open('conditionals/Q17_Largest.py') as subfile:
  sub = ast.parse(subfile.read())
  
for node in ast.walk(sub):
  if isinstance(node, ast.List):
    print('You may not use lists in your solution!')
    exit(1)