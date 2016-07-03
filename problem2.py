#Fibonacci Sequence Using Recursion

array = []

def recur_fib(n):
	if n <= 1:
		return n
	else:
		return(recur_fib(n-1) + recur_fib(n-2))

nterms = int(input("How many terms? "))

if nterms <=0:
	print("Please enter positive number.")
else:
	print ("Fib Seq: ")
	for i in range(nterms):
		array.append(recur_fib(i))

print array