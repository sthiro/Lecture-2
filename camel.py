#Camel case input => firstName
#Snake_case output => first_name
#str.isupper() ,str.casefold()

s = input("camelCase: ")

for c in s:
    replacer = c 
    if replacer.isupper(): #Checks whether it's upper case
        replacer = "_" + replacer.casefold() #make smaller
    
    print(replacer, end="") #Print in the same line
