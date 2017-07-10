# Pig Latin Translator
# Jack Tillotson

#****************************
# MODULE : openFile
# INPUTS : none
# OUTPUTS : text
# DEF : To open the file and get the text.
#****************************
def openFile():
    file = ""
    
    while file == "":
        
        try:
            file = input("Please enter the name of the file you would like to translate (include the .txt): ")
            theFile = open(file, 'r')
            text = theFile.read()
            
        except FileNotFoundError:
            print("That file was not found, please enter the name of an existing file.")
            file = ""
            
    return text


#****************************
# MODULE : makeLines
# INPUTS : text
# OUTPUTS : totalLines
# DEF : To split the text into lines.
#****************************
def makeLines(text):
    translatedLine = ''
    totalLines = ''
    
    for lines in text.split('\n'):
        translatedLine = translate(lines)
        totalLines += translatedLine
        
    return totalLines


#****************************
# MODULE : translate
# INPUTS : lines
# OUTPUTS : translatedLine
# DEF : To put togethor the new translated word.
#****************************
def translate(lines):
    
    translatedWord = ''
    translatedLine = ''
    words = lines.split()
    
    for word in words:
        lowerCase = word.lower()
        indexes = findIndex(word)
        translatedWord += lowerCase[0:indexes[0]]
        
        if word[indexes[0]] >= 'A' and word[indexes[0]] <= 'Z':
            translatedWord += word[indexes[1]].upper()
            
        else:
            translatedWord += word[indexes[1]]
        translatedWord += lowerCase[indexes[1] + 1:indexes[2] + 1]
        translatedWord += lowerCase[indexes[0]:indexes[1]]
        
        if indexes[0] == indexes[1]:
            translatedWord += "way"
            
        else:
            translatedWord += "ay"
        translatedWord += lowerCase[indexes[2] + 1:] + ' '

    translatedLine += translatedWord
        
    return translatedLine + '\n'

#****************************
# MODULE : findIndex
# INPUTS : word
# OUTPUTS : indexes
# DEF : To find first letter, first vowel, and last letter in the word.
#****************************
def findIndex(word):
    indexes = [-1, -1, -1]
    counter = len(word)
    lowerCase = word.lower()

    for i in range(len(word)):
        
        if lowerCase[i] >= 'a' and lowerCase[i] <= 'z' and indexes[0] == -1:
            indexes[0] = i

        if lowerCase[i] in ['a', 'e', 'i', 'o', 'u', 'y'] and indexes[1] == -1:
            
            if lowerCase[i - 1] != 'q':
               indexes[1] = i

    while indexes[2] == -1:
        counter -= 1
        
        if lowerCase[counter] >= 'a' and lowerCase[counter] <= 'z':
            indexes[2] = counter

    return indexes

        
#****************************
# MODULE : showOutput
# INPUTS : totalLines
# OUTPUTS : none
# DEF : To display the translated text to the user.
#****************************
def showOutput(totalLines):
    print(totalLines)

#****************************
# MODULE : saveFile
# INPUTS : totalLines
# OUTPUTS : none
# DEF : To save the translated text to a new file.
#****************************
def saveFile(totalLines):
    newFile = open('ilenamefay.txt', 'w')
    newFile.write(totalLines)
    newFile.close

#****************************
# MODULE : main
# INPUTS : none
# OUTPUTS : none
# DEF : Main function for the program that calls other files.
#****************************
def main():

    text = openFile()
    totalLines = makeLines(text)
    showOutput(totalLines)
    saveFile(totalLines)

main()
