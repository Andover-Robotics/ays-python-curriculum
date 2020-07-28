words = ['with', 'power', 'comes', 'responsibility']
for word in words:
  word += '...'


for i in range(len(words)):
  words[i] += '...'
  if i > 2:
    break

print(words) # what is the output?