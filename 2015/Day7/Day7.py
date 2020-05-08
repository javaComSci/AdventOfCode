import re

filepath = 'data.txt'
with open(filepath) as fp:
   line = fp.readline()
   linesLeft = []
   while line or len(linesLeft) > 0:
        wordsLooking = []
        if line:
            words = re.split('\n| |->',line)
            newWords = []
            for word in words:
                if word != "":
                    newWords.append(word)
            print(newWords)
            wordsLooking = newWords
        else:
            words = re.split('\n| |->',linesLeft[0])
            newWords = []
            for word in words:
                if word != "":
                    newWords.append(word)
            wordsLooking = newWords
            del linesLeft[0]

        if wordsLooking[0] == "NOT":
            if wordsLooking[1] in inputs:
                inputs[wordsLooking[2]] = ~inputs[words[1]]
            else:
                linesLeft.append()
        if(words[0].Equals("NOT")) 