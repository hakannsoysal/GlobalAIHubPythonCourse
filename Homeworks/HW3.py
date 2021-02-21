def prime_first():
    for i in range(1,501):
        if i > 1:
            for j in range(2,i):
                if (i % j) == 0:
                    break

            else:
                print("0-500 arasındaki asal sayılar :",i)    

def prime_second():
    for i in range(500,1001):
        if i > 1:
            for j in range(2,i):
                if(i % j) == 0:
                    break

            else:
                print("500-1000 arasındaki asal sayılar :",i)    

for i in  range(0,1001):
    if i == 500:
        prime_first()
    elif i == 1000:
        prime_second()
        