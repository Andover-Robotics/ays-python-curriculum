import os

try:
  print('According to your program,')
  for case in [[4, 8, 2], [9, 5, 8], [9, 13, 14], [15, 15, 12], [16, 16, 16]]:
    process = os.popen('python3 conditionals/Q17_Largest.py {} {} {}'.format(*case))
    print('The largest of {} is {}'.format(case, process.read().strip()))
except Exception as e:
  print('Error occurred: ' + str(e))