#CONVERTION OF INFIX TO POSTFIX

def convertToPostfix(str):
	stack = []
	op = []
	for i in range(len(str)):
		ch = str[i]
		if ch.isdigit():
			op.append(ch)
		elif ch == '+' or ch == '-':
			if len(stack) != 0:
				old_top = stack.pop()
				op.append(old_top)
			stack.append(ch)
		elif ch == '*' or ch == '/':
			if len(stack) == 0:
				stack.append(ch)
			else:
				old_top = stack[len(stack) -1]
				if old_top == '+' or old_top == '-':
					stack.append(ch)
				elif old_top == '*' or old_top == '/':
					stack.pop()
					op.append(old_top)
					stack.append(ch)
				else:#opening bracket
					stack.append(ch)
		elif ch == '(':
			stack.append(ch)
		elif ch == ')':
			top = stack.pop()
			while top != '(':
				op.append(top)
				top = stack.pop()
		else:
			pass #ignore
		while len(stack) > 0:
			op.append(stack.pop)
		return op

str = input("Enter infix expression: ")
op = convertToPostfix(str)
print(op)
