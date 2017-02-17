#card number check with Lyhn's algorithm
#goals of algorithm is to verify validity of given card number
#how? by summing up all the numbers, while doubling every even number(counting from the end). 
n_string = input("Put yer number 'ere, rascal\n")

sum = 0
for i in range(len(n_string)):
	if i%2==0:
		sum=sum+int(n_string[i])
	else:
		if int(n_string[i])*2 > 9:
			sum=sum+(int(n_string[i])*2-9)
		else:
			sum=sum+(int(n_string[i])*2)

if sum%10==0:
	print("Checksum is ", sum, ", therefore cardnumber is valid")
else:			
	print("Checksum is", sum, "therefore cardnumber is invalid")		