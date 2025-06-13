from random import randint
def check_word(word, word_list):
  return word in word_list
import sys
# Capitalize the first letter of the word CHECK
# Be able to choose the number of words CHECK
# Choose the number of numbers CHECK
# Make format words, symbol, numbers CHECK
# Choose Number of Passwords CHECK
# Cannot Start word with O or L or I CHECK
# symbols can only be ~!@#$%^&*()_+=- CHECK
# choose number of symbols CHECK
# make sure same word is not used twice
with open('words.txt') as f:
  wordLines = f.read()
currentlyUsedWords = set()
words = wordLines.split()

with open('symbols.txt') as f:
  symbolLines = f.read()
#with open('letters.txt') as f:
#  textLines = f.read() 
#text = textLines.split()
symbols = symbolLines.split()
#def getPasswords(passwordAmount, wordAmount, wordLength, numberAmount, symbolAmount, acronym=None):
#  for i in range(passwordAmount):
#    print(getPassword(wordAmount, wordLength, numberAmount, symbolAmount, acronym))
#  return

#def getPassword(wordAmount, wordLength, numberAmount, symbolAmount, acronym):
#  if acronym == None:
#    return getNewPassword(wordAmount, wordLength, numberAmount, symbolAmount)
#  else:
#    return getNewAcronym(wordAmount, wordLength, numberAmount, symbolAmount, acronym)

def getNewPassword():
  global currentlyUsedWords
  currentWordAmount = 0
  currentPassword = ""
  while True:
    #text = letters[randint(0, len(letters) - 1)]
    word = words[randint(0, len(words) - 1)]
    firstLetter = word[0]
    if len(word) == wordLength and firstLetter not in ['o', 'l', 'i', 'O', 'L','I'] and word not in currentlyUsedWords:
      currentWordAmount += 1
      word = word.capitalize()
      currentPassword += word
      currentlyUsedWords.add(word)
      if currentWordAmount == wordAmount:
        for i in range(symbolAmount):
          currentPassword += symbols[randint(0, len(symbols) - 1)]
        for i in range(numberAmount):
          currentPassword += str(randint(0, 9))
        print(currentPassword)
        return
def getNewAcronym():
  global currentlyUsedWords
  currentWordAmount = 0
  currentPassword = ""
  while True:
    word = words[randint(0, len(words) - 1)]
    firstLetter = word[0]
    if len(word) == wordLength and firstLetter in acronym[currentWordAmount] and word not in currentlyUsedWords:
      currentWordAmount += 1
      word = word.capitalize()
      currentPassword += word
      currentlyUsedWords.add(word)
      if currentWordAmount == wordAmount:
        for i in range(symbolAmount):
          currentPassword += symbols[randint(0, len(symbols) - 1)]
        for i in range(numberAmount):
          currentPassword += str(randint(0, 9))
        print(currentPassword)
        return
# def getWord(firstLetter, wordLength):
#  global currentlyUsedWords
#  while True
#    word = words[randint(0, len(words) - 1)]
#    if len(word) == wordLength and word[0] == firstLetter:
#      return word
doAcronym = input("do you want an acronym? y/n ")
if doAcronym == "n":
  passwordAmount = int(input("how many passwords "))
  wordAmount = int(input("how many words "))
  wordLength = int(input("how many letters per word "))
  numberAmount = int(input("how many numbers "))
  symbolAmount = int(input("how many symbols "))
  for i in range(passwordAmount):
    getNewPassword()
if doAcronym == "y":
  acronym = input("what is the acronym ")
  passwordAmount = int(input("how many passwords "))
  wordLength = int(input("how many letters per word "))
  numberAmount = int(input("how many numbers "))
  symbolAmount = int(input("how many symbols "))
  wordAmount = len(acronym)
  for i in range(passwordAmount):
    getNewAcronym()
  
