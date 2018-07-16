import collections

def getMostCommon(words, n):
  counts = collections.Counter(words).most_common(n)
  #print (counts)
  return counts

words = []
with open("document.txt", "r") as f:
  for line in f:
    for word in line.split():
      wordls = word.lower().strip('"\',.?*')
      words.append(wordls)

  result = getMostCommon(words, 10)

for word, count in result:
  print "{0}: {1}".format(word, count)

