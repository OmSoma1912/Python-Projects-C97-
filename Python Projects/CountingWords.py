introString = input ("Enter string :")
characterCount = 0
wordCount = 1
for i in introString:
    characterCount = characterCount + 1
    if (i == ' '):
        wordCount = wordCount + 1
print ("Number of word in string: ")
print (wordCount)
print ("Number of characters in the string :")
print (characterCount)
