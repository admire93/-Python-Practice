def swap(a, b):
    temp = a
    a = b
    b = temp

    return a, b

def bubble():
    num = []
    a = 0
    y = 0
    count = input('input number which input in list')
    
    while y < count:
        x = input('input list.')
        num.append(x)
	y = y+1

    for i in range(count+1):
	if i+1 < count:
            if num[i] > num[i+1]:
                swap(num[i], num[i+1])
		print num
	    else:
	        print num
        else:
	    i = 0
	    count = count-1

    return

bubble()
