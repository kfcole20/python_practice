# Use only the built-in methods and functions from the previous tabs to do the following exercises. You will find the following methods and functions useful:

# • .find()

# • .replace()

# • min()

# • max()

# • .sort()

# • len()

# Find and Replace
# In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". Then create a new string where the word "day" is replaced with the word "month".

words = "It's thanksgiving day. It's my birthday,too!"
print(words.find('day'))
new=words.replace('day','month')
print(new)
# Min and Max
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.
x = [2,54,-2,7,12,98]
print(max(x))
print(min(x))
# First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.
y = ["hello",2,54,-2,7,12,98,"world"]
print(y[0])
print(y[len(y)-1])
# New List
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!repl
z= [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
arr=[]
middle_index = len(z) // 2

first_half = z[:middle_index]
second_half = z[middle_index:]
arr.append(first_half)
for x in range(middle_index, len(z)):
    arr.append(z[x])
print(arr)