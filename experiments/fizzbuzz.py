for i in range (1, 51):
	result = "%s Fizz Buzz" % i
	if i % 3 != 0:
		result = result.replace(" Fizz", "")
	if i % 5 != 0:
		result = result.replace(" Buzz", "")
	print(result)