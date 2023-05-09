# Simple Learning 
# String Concat
print ("hello"+"world!") # o/p hello world!
print ("58"+"45")  # o/p 5845
print (int("58")+int("45"))  # o/p 103
# String with Ends
print("Adios",end="") # No line change will happen
print("Amigos!")
print("Se",end=" ") # No line change will happen space in words
print("Amigos!")
print("Rio",end=" de ") # insert de in between 
print("Zio!")
# String Format  3 ways {valuename} {valueindex} {}
print("Name:{name} and age:{age}".format(name="Zakira",age=41))
print("Name:{0} and age:{1}".format("Zoya",35))
print("Name:{1} and age:{0}".format("Usha",18))     
print("Name:{} and age:{}".format("Akhil",20))
# Second Way formatting  Fast string "f"
samplename,sampleage = "Ramesh",25
print(f"Name:{samplename} and age:{sampleage}")
print(f"Addition of two numbers: {899+745}")
print(f"Let us calculate using different operators: {eval('899+745-45*52//8')}")
# Other string operations
samplestring = "Next-gen Advance python "
print("Let us try lowercase the string",samplestring.lower())
print("Let us try uppercase the string",samplestring.upper())
print("Let us try replacing the string",samplestring.replace("python","AI-python here"))
print (" I am \"friend\" of Yoda")
print (" I am \"friend\" of Yoda \nNot possible")
print (" I am \"friend\" of Yoda \tYes it is")
# List Learning
sample_Varlist = [1,22.345,"Hella",49,49,74,74,-434,"Serpent"]
print("Before Modifying:->",sample_Varlist)
sample_Varlist[-1] = "Victory"
sample_Varlist[2] = 7+6j
print("After Modifying:->",sample_Varlist)
print("Length of the list",len(sample_Varlist))
# sample_Varlist.sort()  TypeError: '<' not supported between instances of 'complex' and 'float'
# print("After Sort of the list",sample_Varlist)
sample_Varlist2 = [2285,49,74,86,49,49,63,74,74,74,12,63,-434,1]
sample_Varlist2.sort()
print("Sorting a integer list",sample_Varlist2)
sample_Varlist3 = [800.23,22.85,8.06,0.49,49.56,-43.4,12.0235]
print("Sorting a floatin list",sample_Varlist3)
sample_Varlist4 = ['c','d','A','R','s','k','e']
print("Sorting a string list",sample_Varlist4)
print("Minimum value in list",min(sample_Varlist4))
print("Maximum value in list",max(sample_Varlist4))
# Conversion
sampleTuple = (1,2,3,4)
sample_Varlist5=list(sampleTuple)
print("tuple to list",sample_Varlist5)
samplestring2 ="EndofWorld"
sample_Varlist5=list(samplestring2)
print("string to list",sample_Varlist5)
sampleset = {1,2,3,4}
sample_Varlist5=list(sampleset)
print("set to list",sample_Varlist5)
print("Before Append to sample_varlist2",sample_Varlist2)
sample_Varlist2.append(685)
print("After Append used to sample_varlist2",sample_Varlist2)
print("Before use of clear sample_varlist5",sample_Varlist5)
sample_Varlist5.clear()
print("After use of clear to sample_varlist5",sample_Varlist5)
# Copying A list
sample_Varlist5 = sample_Varlist2.copy()
print("After use of copy to sample_varlist5",sample_Varlist5)
sample_Varlist2.append("UpdateAfterCopy")
print("After Append used to sample_varlist2",sample_Varlist2)
print("Changes also apply to sample_varlist5",sample_Varlist5)
sample_Varlist5.insert(2086,6)
print("After use of insert at index no 6 to sample_varlist5",sample_Varlist5)
sample_Varlist5.reverse()
print("After use of reverse to sample_varlist5",sample_Varlist5)
sample_Varlist5.pop()
print("After use of pop to sample_varlist5",sample_Varlist5)
sample_Varlist5.pop(2)
print(" pop element at index no 2 to sample_varlist5",sample_Varlist5)
print("using remove to select element sample_Varlist5")
sample_Varlist5.remove(49)
print(" after using remove sample_Varlist5",sample_Varlist5)
print("again using remove to same  element sample_Varlist5")
sample_Varlist5.remove(49)
print(" after using remove sample_Varlist5",sample_Varlist5)
#print(" remove an element not present sample_Varlist5")
#sample_Varlist5.remove(120)  Value Error
print(" one lines multiremove an selected element  present sample_Varlist5")
while 74 in sample_Varlist5:sample_Varlist5.remove(74)
print("New List",sample_Varlist5)
# What is index of number
print("Index of selected element",sample_Varlist5.index(63))
# what is index of 63 if present between 2 and 10
print("Index of the selected element with range given ",sample_Varlist5.index(63,2,10))
# Sum Operation on List
print("List details",sample_Varlist5)
samplesum1 = sum(sample_Varlist5)
print("After sum is used on list",samplesum1)
print("List details",sample_Varlist5)
samplesum2 = sum(sample_Varlist5,55)
print("After sum is used second time on list with addition of 55",samplesum1)
print("List details",sample_Varlist5)
# Range
Samplerangelist = [range(5)]
print("Result it didnot expands",Samplerangelist)
Samplerangelist = [*range(5,15)]
print("Result it expands",Samplerangelist)
Samplerangelist = [*range(5,15,3)]
print("Result it expands with jump of 3",Samplerangelist)
