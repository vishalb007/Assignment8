import threading

def even():
	for i in range(20):
		if(i%2==0):
			print (i)

def odd():
	for i in range(20):
		if(i%2==1):
			print (i)

def main():
	t1=threading.Thread(target=even,args=())
	t2=threading.Thread(target=odd,args=())
	
	t1.start()
	t2.start()

	t1.join()
	t2.join()

if __name__ == "__main__":
	main()