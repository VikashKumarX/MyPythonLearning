# Version :1.0 & purpose: Insert special character in words
# Begin
# taking input from user 
demoword = str(input("Enter a word: "))
# creating an empty list
letter_list = []
# creating an string variable for storing new string
new_wordform = ""
for i in demoword:
    letter_list.append(i)
for k in letter_list:
    if k != letter_list[-1]:
        new_wordform = new_wordform + k + "@"
    else:
        new_wordform += k
# Print new word
print(new_wordform)            
#End