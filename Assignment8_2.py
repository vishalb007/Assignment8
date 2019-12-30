import threading

def evenfactorsum(num):
	sum=0
	for i in range(1,num+1):
		if(num%i==0):
			if(i%2==0):
				sum = sum + i
	print (sum)						

def oddfactorsum(num):
	sum=0
	for i in range(1,num+1):
		if(num%i==0):
			if(i%2==1):
				sum = sum + i
	print (sum)

def main():
	num=int(input("Enter number : "))
	t1=threading.Thread(target=evenfactorsum,args=(num,))
	t2=threading.Thread(target=oddfactorsum,args=(num,))
	
	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print("Exit from main")

if __name__ == "__main__":
	main()