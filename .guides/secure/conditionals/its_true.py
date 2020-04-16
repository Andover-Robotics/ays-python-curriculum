import os, ast
import requests

score = 0
try:
  answer = os.environ['CODIO_FREE_TEXT_ANSWER']
  value = eval(answer)

  # we don't want "truthy"
  if value is True:
    score += 1
    print('👍 Nice: your expression is True')
  else:
    print('👎 Oops: your expression is not True')
  
  syntax_nodes = list(ast.walk(ast.parse(answer)))
  if any(map(lambda node: isinstance(node, ast.Compare), syntax_nodes)):
    score += 1
    print('🎉 Cool: you used one of the boolean expressions!')
  else:
    print('😕 Oops: you did not use one of the boolean expressions.')

except Exception as e:
  print('😦 Something went wrong. Check your syntax: ' + str(e))

print(f'<b style="color:blue">Your score: {score} / 2</b>')
rep = requests.get("{0}&points={1}".format(os.environ['CODIO_PARTIAL_POINTS_URL'], score))