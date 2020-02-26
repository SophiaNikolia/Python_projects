print("Exercise 5\n")
f = open("funfactsfood.txt", "r") #opens the text about fun facts related to food
text = f.read()
print("According to the text:")
print(text,"\n")
punct = '''.,''' #the punctuations that are used in the text above
p = "" #creating the string p that contains everything except for the punctuations above
for i in text: #searching letter by letter
    if i not in punct: #if the letter does not belong to the punctuations above
        p += i  #finding the number of the letters each word has
length = 4
s = []  #creating a list
text = p.split(" ") #spliting the string wherever there is a space
for i in text:
    if len(i) >= length:  #finding whether the word contains more than 3 letters
        s.append(i)  #if it does so, adding the word to the list s
print("The result is:")
for x in range(len(s)):
    print(s[x][1:-1] + s[x][-1:] + s[x][:1] + "ay") #the word without the first letter + the first letter + "ay"
f.close()
