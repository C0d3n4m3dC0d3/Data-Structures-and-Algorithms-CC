def precedence(op):
	if op == '+' or op == '-':
		return 1
	if op == '*' or op == '/':
		return 2
	return 0

def calc(a, b, op):
	if op == '+':
		return a + b
	if op == '-':
		return a - b
	if op == '*':
		return a * b
	if op == '/':
		return a // b

def evaluate(exp):
	values = []
	operators = []

	len_exp = len(exp)
	i = 0

	while i < len_exp:
		if exp[i] == ' ':
			i+=1
			continue

		elif exp[i] == '(':
			operators.append(exp[i])

		elif exp[i].isdigit():
			n = 0
			while ( i<len_exp ) and ( exp[i].isdigit() ):
				n = (n*10)+int(exp[i])
				i+=1
			i-=1
			values.append(n)

		elif exp[i] == ')':
			while ( len(operators) != 0 ) and ( operators[-1] != '(' ):
				b = values.pop()
				a = values.pop()
				op = operators.pop()

				values.append(calc(a, b, op))

			if len(operators) == 0: #mismatched closing brace
				return "Invalid Expression"
			operators.pop()

		else:
			while ( len(operators) != 0 ) and ( precedence(operators[-1]) >= precedence(exp[i]) ):
				if len(values) <= 1: #extra operators
					return "Invalid Expression"
				b = values.pop()
				a = values.pop()
				op = operators.pop()
				values.append(calc(a, b, op))
			operators.append(exp[i])

		i+=1

	while len(operators) != 0:
		if len(values) <= 1: #1 operator and only 1 value
			return "Invalid Expression"
		b = values.pop()
		a = values.pop()
		op = operators.pop()
		if a == None or b == None: #mismatched opening brace
			return "Invalid Expression"
		values.append(calc(a, b, op)) #else, calculate
	return values[0]

if __name__ == '__main__':
	while True:
		exp = input("Enter expression: ")
		print(evaluate(exp))
		flag = input("Continue? y/n - ")
		if flag == 'n' or flag == 'N':
			break
