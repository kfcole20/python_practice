# Assignment: Filter by Type
# Write a program that, given some value, tests that value for its type. Here's what you should do for each type:

# Integer
# If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"

# String
# If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."

# List
# If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."

def filter_type(val):
    if isinstance(val, str) is True:
        if len(val)>=50:
            return "Long Sentence"
        elif len(val)<50:
            return "Short sentence"
        else:
            return "This is empty!"
    elif isinstance(val, int) is True:
        if val>= 100:
            return "That's a big number!"
        else:
            return "That's a small number!"
    elif isinstance(val, list) is True:
        if len(val)>=10:
            return 'Big list!'
        elif len(val)<10:
            return "Short list!"
        else:
            return "The list is empty!s"
    else:
        return "I don't know the type!"
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

print(filter_type(sI))
print(filter_type(mI))
print(filter_type(bI))
print(filter_type(eI))
print(filter_type(spI))
print(filter_type(sS))
print(filter_type(mS))
print(filter_type(bS))
print(filter_type(eS))
print(filter_type(aL))
print(filter_type(mL))
print(filter_type(lL))
print(filter_type(eL))
print(filter_type(spL))