import argparse

def validity(word, rack_list):
    rack_test = list(rack_list)
    w_rd = ""
    for l in word:
        if l in rack_test:
            rack_test.remove(l)
            w_rd += l
        elif "*" in rack_test:
            rack_test.remove("*")
            w_rd += "*"
        else:
            return False, ""
    return True, w_rd

def score(word, scores):
    total = 0
    for l in word:
        total += scores[l]
    return total

def wordFormat(word1, word2):
    if word1 == word2:
        return word1
    else:
        return word1 +" ("+word2+")"

def wordCompare(word1, word2):
    #If one word contains more * than the other, it sorts lower
    #If one word contains more letters than the other, it sorts lower
    if word1.count("*") > word2.count("*"):
        return 1
    elif word1.count("*") < word2.count("*"):
        return -1
    else:
        if len(word1) > len(word2):
            return 1
        elif len(word1) < len(word2):
            return -1
        else:
            return 0

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10, "*": 0}

print "SCRABBLE SOLVER V0.1"

#Construct the word list
SOWPODS_file = open("sowpods.txt", "r")
SOWPODS_raw = SOWPODS_file.readlines()
SOWPODS_file.close()

#Clean up the word list
SOWPODS = [word.strip().lower() for word in SOWPODS_raw]

#Get the rack
parser = argparse.ArgumentParser()
parser.add_argument("rack")
args = parser.parse_args()
rack = args.rack.lower()
print "You've input:", rack
rack_list = list(rack)

#Find valid words and score them
wordScores = {}

for word in SOWPODS:
    valid, w_rd2score = validity(word, rack_list)
    if valid:
        wordScore = score(w_rd2score, scores)
        if wordScores.has_key(wordScore):
            wordScores[wordScore].append(wordFormat(word,w_rd2score))
        else:
            wordScores[wordScore] = [wordFormat(word,w_rd2score)]

#Print words by score
#valid_scores = sorted(wordScores.values(), reverse=True)

allScores = sorted(wordScores, reverse=True)
for i in allScores:
    print "\n" + str(i) + ":"
    for word in sorted(wordScores[i], wordCompare):
        print word
if not allScores:
    print "Exchange some letters!"