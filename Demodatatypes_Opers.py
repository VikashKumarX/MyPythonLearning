#pupose : learning
var1 = 20.3
var2 = int(var1) # Float to int
var3 = complex(var1) # Float to Complex
var4 ='''This is
multiline 
stirng hello
'''
print (" Float value",var1) # Float value 20.3
print (" Int value",var2) #  int value 20
print (" Complex value",var3) # Complex (20.3+0j)
# print("One way of writing sting")
# print('Second way of writing sting')
print("Multi-Line way of writing sting",var4)
'''
Other int values like 1323 -12224 0
Other float values like 1323.2585 -12.224 0.64868
Other complex values like 2j -12-24j 12+2j
'''
# String Slicing index starts from 0 and from backwards index start from -1
mysampleStrng = "Geeks or Nerds"
print("Length of string",len(mysampleStrng)) # 14
print("First letter string",mysampleStrng[0]) # G
print("Seventh letter of string",mysampleStrng[7]) # r
print("Complete string",mysampleStrng[0:len(mysampleStrng)]) # total string
print("Mystery print",mysampleStrng[:]) # total string
print("first different traversal way",mysampleStrng[-5:-1]) # Nerd
print("second different traversal way",mysampleStrng[4:-1]) # s or Nerd
