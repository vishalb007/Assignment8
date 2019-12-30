import threading

def evenlist(num):
	sum=0
	for i in range(len(num)):
		if(num[i]%2==0):
			print(num[i])
			sum = sum + num[i]
	print ("Even sum is : ",sum)						

def oddlist(num):
	sum=0
	for i in range(len(num)):
		if(num[i]%2==1):
			print(num[i])
			sum = sum + num[i]
	print ("Odd sum is : ",sum)	

def main():
	num=[]
	n=int(input("Enter number of elements: "))
	for i in range(n):
		item=int(input())
		num.append(item)
	t1=threading.Thread(target=evenlist,args=(num,))
	t2=threading.Thread(target=oddlist,args=(num,))
	
	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print("Exit from main")

if __name__ == "__main__":
	main()