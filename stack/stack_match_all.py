# Program to check for matching brackets {}()<>[]
# BUG: at line 15 - requires for loop
stack = []
open = ['(', '[', '{']
close = [')', ']', '}']

def matching_all(str):
	for i in range(len(str)):
		if str[i] in open:
			stack.append(str[i])
		elif str[i] in close:
			if len(stack) == 0:
				return False
			else:
				c = stack.pop()

		else:
			pass
	return len(stack) == 0

str = input("Enter string: ")
print("Matching" if matching_all(str) else "Not Matching")
