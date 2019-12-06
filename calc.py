choice = str(input("Choose calculator- programmer or scientific? "))
def programmer():

	num = int(input("Input a number:"))
	if num < 0:
		print("Invalid input")
	binarylist=[]

	while num > 0:
		rem=num%2
		binarylist.append(rem)
		num=num//2

	if num == 0:
		binarylist.reverse()
		print(binarylist)
		print("done")
		ask = str(input("Would you like to continue (y or n)? "))
		if ask == y:
			programmer()		
			return
		if ask == n:
			print("done")

def scientific():

	scientific = str(input("Choose an operator (+,-,*,/,**):"))
	
	if scientific == "+":
		operand1 = float(input("Input the first number:"))
		operand2 = float(input("Input the second number:"))
		ans = (operand1 + operand2)
		print(ans)
		ask = str(input("Would you like to continue (y or n)? "))
		if ask == y:
			programmer()
			return
		if ask == n:
			print("done")
			
	elif scientific == "-":
		operand1 = float(input("Input the first number:"))
		operand2 = float(input("Input the second number:"))
		ans = (operand1 - operand2)
		print(ans)
		ask = str(input("Would you like to continue (y or n)? "))
		if ask == y:
			programmer()
			return
		if ask == n:
			print("done")
	elif scientific == "*":
		operand1 = float(input("Input the first number:"))
		operand2 = float(input("Input the second number:"))
		ans = (operand1 * operand2)
		print(ans)
		ask = str(input("Would you like to continue (y or n)? "))
		if ask == y:
			programmer()
			return
		if ask == n:
			print("done")
	elif scientific == "/":
		operand1 = float(input("Input the first number:"))
		operand2 = float(input("Input the second number:"))
		ans = (operand1 / operand2)
		print(ans)
		ask = str(input("Would you like to continue (y or n)? "))
		if ask == y:
			programmer()
			return
		if ask == n:
			print("done")

	elif scientific == "**":
		operand1 = float(input("Input the first number:"))
		operand2 = float(input("Input the second number:"))
		ans = (operand1 ** operand2)
		print(ans)
		ask = str(input("Would you like to continue (y or n)? "))
		if ask == y:
			programmer()
			return
		if ask == n:
			print("done")
	else:
		print("try again")
def Calculator():
	if choice == programmer:
		run programmer()
	if choice == scientific:
		run scientific()
Calculator()
