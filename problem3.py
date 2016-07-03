#Finding largest prime factors

n = int(raw_input("What number? "))
i = 2
while i * i < n:
	while n % i == 0:
		n = n / i
	i = i + 1

print (n)