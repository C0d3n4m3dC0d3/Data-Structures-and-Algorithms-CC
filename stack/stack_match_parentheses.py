# Program to check if input value has matching parantheses

stack = []

str = input()

def matching(str):
	for i in range(len(str)):
		if str[i] == '(':
			stack.append('(')
		elif str[i] == ')':
			if len(stack) == 0:
				return False
			else:
				stack.pop()
		else:
			pass
	return True if len(stack) == 0 else False

match = matching(str)
print("Matching" if match else "Not Matching")
