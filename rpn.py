#!/usr/bin/env python3

stack = []
def calculate(arg):
	if(arg == '+'):
		arg2 = stack.pop()
		arg1 = stack.pop()
		stack.append(int(arg2) +int(arg1))
	else:
		stack.append(arg)
	print(stack)
	s =answer()
	print(s)
def answer():
	s = stack.pop()
	print(s)
	stack.append(s)
	return s		
def main():
	while True:
 		calculate(input("rpn calc> "))
if __name__ == '__main__': # Note: that's "underscore underscore n a m e ..."
	main()


