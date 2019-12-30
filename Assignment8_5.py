import threading

def display():
	for i in range(1,51):
		print (i)

def reverse():
	i=50
	while(i>0):
		print(i)
		i=i-1

def main():
	t1=threading.Thread(target=display,args=())
	t2=threading.Thread(target=reverse,args=())
	
	t1.start()
	t1.join()

	t2.start()
	t2.join()

if __name__ == "__main__":
	main()