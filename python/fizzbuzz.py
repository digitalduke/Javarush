for i in range(100):
	messsage=''
	if (i+1) % 3 == 0:
		messsage += 'Fizz'
	if (i+1) % 5 == 0:
		messsage += 'Buzz'
	if not messsage:
		messsage = i+1
	print(messsage)
