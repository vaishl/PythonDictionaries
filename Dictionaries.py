d = dict()

def word_counter(d):
  f = open("doc1.txt", "r")
  f = f.read()
  f = f.split()
  for i in f:
    if i not in d:
      d[i] = 1
    else:
      d[i] = d[i] + 1
  print(d)
  print( "The total number of words is " + str(len(d)))
  
  
word_counter(d)