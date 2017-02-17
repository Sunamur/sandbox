#take at ROT13 algorithm
def rot13(string, index):
	new_string = ""
	for letter in string:
		cn = ord(letter) #cn stands for "character number"
		ncn = cn + index #ncn stands for "new character number"
		if ncn > 122: #"if" is there to transform linear alphabet to cyclical
			ncn = ncn-26
		elif ncn < 97: #in case index is negative
			ncn = ncn+26
		new_letter = chr(ncn)
		new_string = new_string + new_letter
	return new_string
	
	

#BIGDIGITS - from Seinfield book
number_dict={10: "..00.. ", 11: "...1.. ", 12: "..22.. ", 13: "..33.. ", 14: "....4. ", 15: ".55555 ", 16: "....6. ", 17: "777777 ", 18: "..88.. ", 19: "...99. ", 20: ".0..0. ", 21: "..11.. ", 22: ".2..2. ", 23: ".3..3. ", 24: "...44. ", 25: ".5.... ", 26: "...6.. ", 27: ".....7 ", 28: ".8..8. ", 29: ".9...9 ", 30: "0....0 ", 31: "...1.. ", 32: "....2. ", 33: "...3.. ", 34: "..4.4. ", 35: ".5.... ", 36: "..6... ", 37: "....7. ", 38: ".8..8. ", 39: ".9...9 ", 40: "0....0 ", 41: "...1.. ", 42: "...2.. ", 43: "..3... ", 44: ".44444 ", 45: ".5555. ", 46: ".666.. ", 47: "...7.. ", 48: "..88.. ", 49: "..999. ", 50: "0....0 ", 51: "...1.. ", 52: "..2... ", 53: "...3.. ", 54: "....4. ", 55: ".....5 ", 56: "6...6. ", 57: ".777.. ", 58: ".8..8. ", 59: "...9.. ", 60: ".0..0. ", 61: "...1.. ", 62: ".2.... ", 63: ".3..3. ", 64: "....4. ", 65: ".5...5 ", 66: "6...6. ", 67: "..7... ", 68: ".8..8. ", 69: "..9... ", 70: "..00.. ", 71: ".1111. ", 72: "222222 ", 73: ".333.. ", 74: "....4. ", 75: ".5555. ", 76: ".66... ", 77: "..7... ", 78: "..88.. ", 79: ".9.... "}
asterisk_dict={10 :"..**.. ",  
                    11 :"...*.. ",  
                    12 :"..**.. ",  
                    13 :"..**.. ",  
                    14 :"....*. ",  
                    15 :".***** ",  
                    16 :"....*. ",  
                    17 :"****** ",  
                    18 :"..**.. ",  
                    19 :"...**. ",  
                    20 :".*..*. ",  
                    21 :"..**.. ",  
                    22 :".*..*. ",  
                    23 :".*..*. ",  
                    24 :"...**. ",  
                    25 :".*.... ",  
                    26 :"...*.. ",  
                    27 :".....* ",  
                    28 :".*..*. ",  
                    29 :".*...* ",  
                    30 :"*....* ",  
                    31 :"...*.. ",  
                    32 :"....*. ",  
                    33 :"...*.. ",  
                    34 :"..*.*. ",  
                    35 :".*.... ",  
                    36 :"..*... ",  
                    37 :"....*. ",  
                    38 :".*..*. ",  
                    39 :".*...* ",  
                    40 :"*....* ",  
                    41 :"...*.. ",  
                    42 :"...*.. ",  
                    43 :"..*... ",  
                    44 :".***** ",  
                    45 :".****. ",  
                    46 :".***.. ",  
                    47 :"...*.. ",  
                    48 :"..**.. ",  
                    49 :"..***. ",  
                    50 :"*....* ",  
                    51 :"...*.. ",  
                    52 :"..*... ",  
                    53 :"...*.. ",  
                    54 :"....*. ",  
                    55 :".....* ",  
                    56 :"*...*. ",  
                    57 :".***.. ",  
                    58 :".*..*. ",  
                    59 :"...*.. ",  
                    60 :".*..*. ",  
                    61 :"...*.. ",  
                    62 :".*.... ",  
                    63 :".*..*. ",  
                    64 :"....*. ",  
                    65 :".*...* ",  
                    66 :"*...*. ",  
                    67 :"..*... ",  
                    68 :".*..*. ",  
                    69 :"..*... ",  
                    70 :"..**.. ",  
                    71 :".****. ",  
                    72 :"****** ",  
                    73 :".***.. ",  
                    74 :"....*. ",  
                    75 :".****. ",  
                    76 :".**... ",  
                    77 :"..*... ",  
                    78 :"..**.. ",  
                    79 :".*.... "}
def bigdigits():
#to be filled with chars for digits. indices are two-digit numbers, where 1st is row (1 to 7), second is actual number (0 to 9)
	input_digits=input("put your number here: ")
	input_dict=input("choose your format: 1 for asterisk, 2 for digits")
	if input_dict=="1":
		dct=asterisk_dict
	else:
		dct=number_dict
	rows = ["","","","","","",""]
	for digit in input_digits:
		for row in range(0, 7):
			digit=int(digit)
			rows[row] += dct[(row+1)*10+digit]
	for count in range(7):
		print(rows[count])
		
		
		

#lucky ticket checker in 3 parts: validator, executable and reporter
#by launching lucky_ticket_report we can count the chance of ticket being lucky in given range


def lucky_valid(num1, num2):
    a = sum(map(int,list(str(num1))))
    b = sum(map(int,list(str(num2))))
    while a>9:
        a = sum(map(int,list(str(a))))
    while b>9:
        b = sum(map(int,list(str(b))))
    if a==b:
        return True
    else:
        return False

def lucky(number):
    slicer = int(len(str(number)))#universal-count execution
    if slicer==1:
        num1 = 0
        num2 = number
    else:
        hslicer = int(slicer/2)#h stands for half
        num1 = int(str(number)[:hslicer])
        num2 = int(str(number)[hslicer:])
    return lucky_valid(num1, num2)
        
def lucky_ticket_report(limit):#last function - check and report for lucky tickets in given range
    counter = 0
    true = 0
    false = 0
    for i in range(limit):
        counter+=1
        if lucky(i)==True:
            true+=1
        if lucky(i)==False:
            false+=1
    print("Total count of numbers:", counter)
    print("total lucky ticket number is:", true)
    print("Lucky percentage is:", (true/counter)*100, "%")
            
