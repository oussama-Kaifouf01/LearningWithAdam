text = "hello, I have 4 oranges"
#get the first element of text
print(text[0])
#get the last element using len() function
print(text[len(text) - 1])
#replace a letter from text
text = text.replace("4","8")
text = text.replace("oranges","apples")
print(text)
#turn all letters in uppercase
text = text.upper()
print(text)
#get the index of a specific word or letter
print(text.find("O"))