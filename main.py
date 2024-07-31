def main():
        path = "books/frankenstein.txt"
        text_content = getText(path)
        num_words = countWords(text_content)
        fCharDict = countCharDict(text_content)
        sortedList = getSortedDict(fCharDict)
        sortDict = sortedList.sort(reverse=True, key=sort_on)
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{num_words} words in the document")
        print("")

        for dict in sortedList:
            print(f"The {dict['name']} character was found {dict['num']} times.")
        
        print("")
        print("---End of the report---")

def getSortedDict(dict):
    sorted = []
    for key in dict:
        value = dict[key]
        dict2 = {"name": key, "num": value}
        sorted.append(dict2)
    return sorted

def sort_on(dict):
    return dict["num"]

def getText(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def countWords(text):
    words = text.split()
    return len(words)

def countCharDict(text):
    charDict = {}
    textLow = text.lower()
    for c in textLow:
        if c.isalpha():
            if c not in charDict:
                charDict[c] = 1
            else:
                charDict[c] += 1
    return charDict


main()