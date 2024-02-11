num=int(input())
num_set=set()
factors=set()
def int_values(number):
    for i in number:
        num_set.add(int(i))
lucky_num={4,7}
int_values(str(num))
if len(num_set)==2 and num_set.issubset(lucky_num)==1:
        print("YES")
elif len(num_set)==1 and num_set.issubset(lucky_num)==1:
     print("YES")
else:
    num_set=set()
    for x in range(1,num):
        if num%x==0:
            print(x)
            factors.add(x)
            print(factors)
            int_values(str(x))
            if num_set.intersection(lucky_num)==1:
                print("YES")
            else:
                print("NO")

        

