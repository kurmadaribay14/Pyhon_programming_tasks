from re import split

def ProcessLine(Words, WordText):
    for Word in Words:
        if Word in WordText:
            WordText[Word] += 1
        else:
            WordText[Word] = 1

def ProcessText(WordText):
    TempList = []
    for key, value in WordText.items():
        TempList.append((value, key))

    TempList.sort()
    return TempList


def FormatPrint(InputList, reverse, WordNum):
    if reverse:
        InputList.sort(reverse=True)

    print "\n", "%-16s %s %16s" % ("Word", "|", "Count"), "\n"
    for count, word in InputList:
        print "%-16s %s %16d" % (word, "|", count)


def WordCount(File, MaxToMin=False):
    txt = open("text.txt", "r")
    WordText = {}
    for line in txt:
        if line.replace("", "") != ("\n" or None):
            ProcessLine(filter(None, split("[^a-zA-Z']+", line.lower())), WordText)

    txt.close()
    FinalList = ProcessText(WordText)
    FormatPrint(FinalList, MaxToMin, len(WordText))


WordCount("C:/text.txt", True)
