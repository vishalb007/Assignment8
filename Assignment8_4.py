import threading

def small(string):
	sum=0
	for i in range(len(string)):
		if(string[i].islower()):
			sum = sum + 1
	print ("Small number is : ",sum)						

def capital(string):
	sum=0
	for i in range(len(string)):
		if(string[i].isupper()):
			sum = sum + 1
	print ("Capital number is : ",sum)	

def digit(string):
	sum=0
	for i in range(len(string)):
		if(string[i].isdigit()):
			sum = sum + 1
	print ("Digit number is : ",sum)

def main():
	string=input("Enter the string : ")
	t1=threading.Thread(target=small,args=(string,))
	t2=threading.Thread(target=capital,args=(string,))
	t3=threading.Thread(target=digit,args=(string,))

	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()

	print("Exit from main")

if __name__ == "__main__":
	main()