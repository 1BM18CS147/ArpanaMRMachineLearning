print("Enter two numbers")
a,b=map(int,raw_input().split())
print("Enter operation:+,-,/,*,%")
op=raw_input().rstrip()


if op== "+":
	print(a+b)
elif op == "-":
	print(a-b)
elif op == "/":
	print(a/b)
elif op == "*":
	print(a*b)
elif op == "%":
	print(a%b)
else:
	print("Try again") 
