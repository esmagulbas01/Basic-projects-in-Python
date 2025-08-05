fibonacci=int(input("Enter a number of fibonacci elements:  "))

if(fibonacci<=0):
    print("Enter a positive number: ")
else:
    fibonacci_list=[]
    first=0
    second=1
    for _ in range(fibonacci):
        fibonacci_list.append(first)
        temp=first+second
        first=second
        second=temp
    print(f"The first {fibonacci} elements of the fibonocci series {fibonacci_list} ")    





  