introduction = input("Enter your introduction")
print(introduction)
numberOfCharacters = 0
numberOfWords = 0

for i in introduction : 
        numberOfCharacters = numberOfCharacters+1
        if (i == ' ') :
            numberOfWords=numberOfWords+1


print("number of characters :", numberOfCharacters)
print("number of words: ", numberOfWords)
# This is for comment




