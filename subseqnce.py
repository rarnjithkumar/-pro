def loa(arr,r): 
	m=1
	l=1
	for i in range(1,r) : 
		if(arr[i]>arr[i-1]): 
			l=l+1
		else:
			if(m<l): 
				m=l 
			l=1
	if(m<l) : 
		m=l 
	return m 
r=int(input()) 
arr =list(map(int,input().split()))
print(loa(arr,r)) 
