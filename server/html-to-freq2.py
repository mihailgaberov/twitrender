# html-to-freq-2.py

import urllib
import obo

url = 'https://mihail-gaberov.eu/how-i-build-desktop-chat-app-with-cometchat-and-nwjs/'

response = urllib.urlopen(url)
html = response.read()
text = obo.stripTags(html).lower()
fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

for s in sorteddict: print(str(s))
