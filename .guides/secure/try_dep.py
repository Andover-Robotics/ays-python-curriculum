import sys
from unittest.mock import MagicMock

def wormhole(a): pass
sysp, print = print, wormhole

for var in sys.argv[1].split(','):
  exec("{} = MagicMock()".format(var))

with open(sys.argv[2]) as sub:
  exec(sub.read())
